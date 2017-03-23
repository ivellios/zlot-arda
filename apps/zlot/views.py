# -*- coding: utf-8 -*-
# Create your views here.

from models import *
from static.models import *
from zapisy.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404 


def informacje(request,text='o-zlocie'):
  i = get_object_or_404(StaticContent,slug=text)
  return render_to_response('static/show_static.html',{'static_content':i}, context_instance=RequestContext(request))

#def plemiona(request):
#  p = Plemie.objects.all()
#  return render_to_response('zlot/plemiona.html',{'plemiona':p},context_instance=RequestContext(request))

def dokumenty(request):
  d = Dokument.objects.filter(mozna_pobrac = True).order_by('id')
  return render_to_response('zlot/dokumenty.html',{'dokumenty':d},context_instance=RequestContext(request))

def ktojedzie(request, rok=2012): 
  u = Plemie.objects.filter(can_register=True)
  for z in u:
    z.zapisani = Uczestnik.objects.filter(uczestnictwo__zlot__rok=rok,uczestnictwo__plemie=z.id)
  return render_to_response('zlot/ktojedzie.html',{'plemiona':u},context_instance=RequestContext(request))

def voting(request, hashset):
    voter = get_object_or_404(Voter, hashset = hashset)
    if voter.vote:
        return render_to_response('zlot/voting_already_voted.html',{'voter':voter},context_instance=RequestContext(request))
    return render_to_response('zlot/voting.html',{'voter':voter},context_instance=RequestContext(request))

def vote(request, hashset):
    voter = get_object_or_404(Voter, hashset = hashset,)
    if voter.vote:
        return render_to_response('zlot/voting_already_voted.html',{'voter':voter},context_instance=RequestContext(request))
    if request.method == "POST":
        v = request.POST.get('vote', None)
        if v:
            voter.vote = v
            voter.save()
            return render_to_response('zlot/voting_success.html',{'voter':voter},context_instance=RequestContext(request))
    raise Http404

from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
import time
def send_votes(request):
    messages = []

    connection = get_connection() # uses SMTP server specified in settings.py
    connection.open() # If you don't open the connection manually, Django will automatically open, then tear down the connection in msg.send()
    x = 0
    for voter in Voter.objects.all():
        html_content = render_to_string('zlot/vote_email.html', {'voter': voter,})               
        text_content = "..."
        msg = EmailMultiAlternatives(u"Głosowanie na organizatorów Zlotu Arda 2015", text_content, "ivellios@arda.org.pl", [voter.email, ], connection=connection)                                      
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        x += 1
        if x % 10 == 0:
            connection.close()
            connection = get_connection()
            connection.open()


    connection.close() # Cleanup
    return render_to_response('zlot/voting_success.html',{'voter':voter},context_instance=RequestContext(request))







