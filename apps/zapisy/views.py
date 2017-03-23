# -*- coding:utf-8 -*-
# Create your views here.
from smtplib import SMTPDataError
from forms import *
from django.shortcuts import render_to_response,get_object_or_404
from mailing.func import *
from django.http import HttpResponse,Http404
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
#from django.views.generic.simple import render

from django.core.mail import mail_managers # mailing system
from django.core.mail import EmailMultiAlternatives # advanced mailing system
from django.template.loader import render_to_string
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMessage
from md5 import md5
from models import *
from django.template.loader import render_to_string

from django.views.generic import TemplateView

class LarpView(TemplateView):
    template_name = 'zapisy/larp.html'

    def get_context_data(self, **kwargs):
        context = super(LarpView, self).get_context_data(**kwargs)
        context['larp'] = get_object_or_404(Larp, slug = kwargs.get('slug'))
        return context

def show_frakcja(request, lslug, fslug):
    frakcja = get_object_or_404(Frakcja, slug = fslug, dostepny_opis = True, larp__slug = lslug)
    return render_to_response('zapisy/frakcja.html', {'frakcja': frakcja}, context_instance = RequestContext(request))

@login_required
def zapis_do_frakcji(request, lslug, fslug):
    frakcja = get_object_or_404(Frakcja, slug = fslug, dostepny_opis = True, larp__slug = lslug, mozna_wybrac = True)
    if not frakcja.larp.zapisy_otwarte: # nie może się zapisać
        raise Http404
    try: # sprawdź, czy już sie nie zapisywał
        frakcjazapis = FrakcjaUczestnik.objects.get(uczestnik = request.user.uczestnik, frakcja__larp = frakcja.larp)
        return render_to_response('zapisy/zapis_do_frakcji_juz_zapisany.html', {'frakcja': frakcja}, context_instance = RequestContext(request))
    except FrakcjaUczestnik.DoesNotExist:
        pass
    if request.method == "POST": # dokonaj zapisu
        FrakcjaUczestnik.objects.create(frakcja=frakcja, uczestnik = request.user.uczestnik)
        return render_to_response('zapisy/zapis_do_frakcji_done.html', {'frakcja': frakcja}, context_instance = RequestContext(request))
    return render_to_response('zapisy/zapis_do_frakcji.html', {'frakcja': frakcja}, context_instance = RequestContext(request))

@login_required
def show_frakcja_list(request):
    wybrane_frakcje = FrakcjaUczestnik.objects.filter(uczestnik = request.user.uczestnik)
    return render_to_response('zapisy/wybrane_frakcje.html', {'frakcje': wybrane_frakcje}, context_instance = RequestContext(request))

def nowy_zapis(request, rok):
    if request.user.is_authenticated(): # jeżeli użytkownik jest zalogowany ma uproszczony zapis
        return redirect('/konto/zapis/'+rok)
    zlot = get_object_or_404(Zlot, rok = rok)
    if request.method == "POST": # przetworzenie formularza
        uczestnictwo = Uczestnictwo(zlot = zlot) # stworzenie instancji uczestnictwa
        form = NoweUczestnictwoForm(request.POST, instance = uczestnictwo) # formularz
        if form.is_valid(): # jeżeli formularz dobrze wypełniony
            user = Uczestnik(username = form.cleaned_data['username'], email = form.cleaned_data['email']) 
            user.set_password(form.cleaned_data['password'])
            user.save()
            form.instance.uczestnik = user
            form.save()
            subject, from_email, to = u"Zapisałeś się na Zlot Arda", 'no-reply@arda.org.pl', user.email
            html_content = render_to_string('zapisy/mailing/potwierdzenie.html', { 'uczestnictwo' : uczestnictwo, 'zlot':zlot  })
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            try:
                msg.send() # wysyłamy e-mail
            except SMTPDataError:
                pass

            subject, from_email, to = u"Zapis na "+zlot.__unicode__(), 'no-reply@arda.org.pl', 'ravenne@arda.org.pl'
            html_content = render_to_string('zapisy/mailing/informacja.html', { 'uczestnictwo' : form.instance, 'form': form, 'zlot': zlot  })
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            try:
                msg.send() # wysyłamy do administracji
            except SMTPDataError:
                pass
            subject, from_email, to = u"Zapis na "+zlot.__unicode__(), 'no-reply@arda.org.pl', 'postacie@arda.org.pl'
            html_content = render_to_string('zapisy/mailing/informacja.html', { 'uczestnictwo' : form.instance, 'form': form, 'zlot': zlot  })
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            try:
                msg.send() # wysyłamy do administracji
            except SMTPDataError:
                pass
            return render_to_response('zapisy/dziekujemy.html',{'nick':form.cleaned_data['username'],'zlot':zlot}, context_instance = RequestContext(request))
    else:
        form = NoweUczestnictwoForm()
    return render_to_response('zapisy/zapis.html',{'formularz':form,'zlot':zlot}, context_instance = RequestContext(request))

@login_required
def zapis(request, rok):
    try:
        user = Uczestnik.objects.get(id=request.user.id)
    except Uczestnik.DoesNotExist:
        redirect('/konto/login/?next=/konto/zapis/'+rok)
    zlot = get_object_or_404(Zlot,rok=rok)
    try: # jeżeli już się zapisał na Zlot to dziękujemy
        uczestnictwo = Uczestnictwo.objects.get(uczestnik=user, zlot=zlot)
        return render(request, 'zapisy/juz_zapisany.html', {'zlot':zlot})
    except Uczestnictwo.DoesNotExist: # w innym przypadku pozwalamy na zapis
        if request.method == "POST": # gdy się zapisuje...
            uczestnictwo = Uczestnictwo(zlot = zlot, uczestnik = user)
            form = UczestnictwoForm(request.POST, instance = uczestnictwo)
            if form.is_valid():
                form.save()
                subject, from_email, to = u"Zapisałeś się na "+zlot.__unicode__(), 'no-reply@arda.org.pl', user.email
                html_content = render_to_string('zapisy/mailing/potwierdzenie.html', { 'uczestnictwo' : form.instance, 'zlot': zlot  })
                msg = EmailMultiAlternatives(subject, '', from_email, [to])
                msg.attach_alternative(html_content, 'text/html')
                try:
                    msg.send() # wysyłamy potwierdzenie
                except SMTPDataError:
                    pass

                subject, from_email, to = u"Zapis na "+zlot.__unicode__(), 'no-reply@arda.org.pl', 'ivellios@arda.org.pl'
                html_content = render_to_string('zapisy/mailing/informacja.html', { 'uczestnictwo' : form.instance, 'form': form, 'zlot': zlot  })
                msg = EmailMultiAlternatives(subject, '', from_email, [to])
                msg.attach_alternative(html_content, 'text/html')
                try:
                    msg.send() # wysyłamy do administracji
                except SMTPDataError:
                    pass
                subject, from_email, to = u"Zapis na "+zlot.__unicode__(), 'no-reply@arda.org.pl', 'postacie@arda.org.pl'
                html_content = render_to_string('zapisy/mailing/informacja.html', { 'uczestnictwo' : form.instance, 'form': form, 'zlot': zlot  })
                msg = EmailMultiAlternatives(subject, '', from_email, [to])
                msg.attach_alternative(html_content, 'text/html')
                try:
                    msg.send() # wysyłamy do administracji
                except SMTPDataError:
                    pass
                return render_to_response('zapisy/dziekujemy.html',{'nick':user.username,'zlot':zlot}, context_instance = RequestContext(request))
        else:
            form = UczestnictwoForm()
        return render_to_response('zapisy/zapis_again.html',{'formularz':form,'uczestnik':user,'zlot':zlot}, context_instance = RequestContext(request))

# deprecated
def wyslij_kody(request,hash):
    if hash=='supertajnykodnieznanynikomu':
        for uczestnik in Uczestnik.objects.filter(email_sent=False):
            zlot = Zlot.objects.get(rok=2011)
            subject, from_email, to = u"Zapisz się na Zlot Arda 2011", 'no-reply@arda.org.pl', uczestnik.email
            text_content = render_to_string('zapisy/mailing/zapisz_sie.txt', { 'uczestnik' : uczestnik, 'zlot':zlot })
            html_content = render_to_string('zapisy/mailing/zapisz_sie.html', { 'uczestnik' : uczestnik, 'zlot':zlot  })
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            try:
                msg.send()
                uczestnik.email_sent = True
                uczestnik.save()
            except SMTPDataError:
                pass
        return HttpResponse('wyslane')
    else:
        raise Http404

def get_hash(request,userid):
    user = get_object_or_404(Uczestnik,id=userid)
    return HttpResponse(user.get_register_hash())

#deprecated
def info(request):
    if raportDoRekruterow():
        return HttpResponse("Wyslane")
    else:
        return HttpResponse("Blad")

# deprecated
def infoUcz(request):
    o = Uczestnik.objects.all()
    m = [i.email+', ' for i in o]
    return HttpResponse(m)

    
#USERS

def zloty_login(request): # logowanie do serwisu
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next=request.GET.get('next',None)
                    if next:
                        return redirect(next)
                    return redirect('/')
    return render(request, 'zapisy/login.html', {'login_form': login_form})

@login_required
def zloty_logout(request): # wylogowanie z serwisu
    logout(request)
    return redirect('/')

# deprecated    
@login_required
def zloty(request): 
    return render(request, 'zapisy/zloty.html', {})

@login_required
def change_password(request,): # zmiana hasla
    form = ChangePasswordForm()
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.set_password(form.cleaned_data['new_password'])
            request.user.save()
            msg = u"Hasło zostało zmienione."
            return render(request, 'zapisy/password_reset_confirm.html', {'msg': msg })
    return render(request, 'zapisy/change_password.html', {'form': form })
    

def reset_password(request, uid=None, code=None): # reset hasla
    if not code:
        if request.method == "POST":
            try:
                user = Uczestnik.objects.get(email=request.POST.get('email',None))
            except Uczestnik.DoesNotExist:
                msg = u"Nie znaleziono użytkownika zarejestrowanego na ten adres email"
                return render(request, 'zapisy/password_reset_confirm.html', {'msg': msg })
            
            #wysłanie kodu
            code = md5("zmianahaslatajnyseed"+str(user.email)+str(user.username)).hexdigest()

            # TODO: przeniesc do template
            codestring = u"""Witaj, """+ str(user.username)+u"""
            
            Poproszono o przypomnienie Twojego hasła. 
            
            Aby odzyskać hasło wejdź na adres: http://arda.org.pl/konto/haslo/reset/"""+str(user.id)+"""/"""+code+u"""/
            
            Jeżeli nie prosiłeś(aś) o zmianę hasła, zignoruj tę wiadomość."""
            
            send_mail('Zlot Arda - Reset hasła', codestring, 'no-reply@arda.org.pl', [user.email], fail_silently=True)
            msg = u"Link do odzyskania hasła wysłano na twoją skrzynkę pocztową"
            return render(request, 'zapisy/password_reset_confirm.html', {'msg': msg })
        return render(request, 'zapisy/password_reset_confirm.html')
    else:
        user = get_object_or_404(Uczestnik,id=uid)
        right_code = md5("zmianahaslatajnyseed"+str(user.email)+str(user.username)).hexdigest()
        if right_code == code:
            form = ResetPasswordForm()
            if request.method == "POST":
                form = ResetPasswordForm(request.POST)
                if form.is_valid():
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    msg = u"Hasło zostało zmienione. Możesz się zalogować"
                    return render(request, 'zapisy/password_reset_confirm.html', {'msg': msg })
            return render(request, 'zapisy/change_password.html', {'form': form })
        raise Http404

@login_required
def lista_zapisanych(request, rok): # wyswietla liste osob zapisanych na dany rok
    zlot = get_object_or_404(Zlot, rok = rok)
    uczestnicy = zlot.uczestnictwo_set.all()
    lista = ', '.join([u.uczestnik.email for u in uczestnicy])
    return HttpResponse(lista)

def lista_bez_frakcji(request, larp_slug): # wyswietla liste osob nie zapisanych do frakcji
    larp = get_object_or_404(Larp, slug=larp_slug)
    zapisani = []
    for fu in FrakcjaUczestnik.objects.filter(frakcja__larp=larp):
        zapisani.append(fu.uczestnik.id)
    niezapisani = Uczestnictwo.objects.filter(zlot__rok=2013).exclude(uczestnik__id__in=zapisani)
    return HttpResponse(', '.join([u.uczestnik.email for u in niezapisani]))

@login_required
def frakcja_wpisy(request, frakcja_id): # wyswietla stronę frakcji i pozwala dodawać wpisy w dyskusji
    fu = get_object_or_404(FrakcjaUczestnik, frakcja = frakcja_id, uczestnik = request.user.uczestnik)
    if request.method == "POST":
        awf = AddWpisForm(request.POST)
        if awf.is_valid():
            awf.instance.fu = fu
            awf.save()
            receivers_fu = FrakcjaUczestnik.objects.filter(frakcja = fu.frakcja).exclude(id=fu.id)
            for receiver in receivers_fu:
                message = render_to_string('zapisy/mailing/dyskusja_wpis.html', {'fu': fu, 'wpis': awf.instance, 'user': request.user.uczestnik })
                msg = EmailMessage("Dodano wpis do twojej frakcji", message, 'no-reply@arda.org.pl', [receiver.uczestnik.email])
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send()
    awf = AddWpisForm()
    dl = Wpis.objects.filter(fu__frakcja=fu.frakcja)
    return render(request, 'zapisy/dyskusja.html', {'form': awf, 'lista_wpisow': dl, 'fu': fu})