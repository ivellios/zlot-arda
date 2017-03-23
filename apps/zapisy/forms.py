# -*- coding: utf-8 -*-

from django.forms import ModelForm,ValidationError
from django import forms
from models import *

class UczestnictwoForm(ModelForm):
    #plemie = forms.ModelChoiceField(queryset=Plemie.objects.filter(can_register=True))
    larp_uczestnictwo = forms.ChoiceField(widget=forms.Select, choices = (('tak', 'Tak'), ('nie', 'Nie')))
    larp_postac = forms.ChoiceField(widget=forms.Select, choices = (('zadna', u'Wybierz'), ('gotowa', u'Wybiorę gotową postać'), ('wlasna',u'Chcę stworzyć własną postać')))

    def clean_od(self):
        od = self.cleaned_data['od']
        if od is not None:
            if od < self.instance.zlot.start:
                raise ValidationError(u'Nie możesz podać daty przed %s' % str(self.instance.zlot.start))
            if od > self.instance.zlot.koniec:
                raise ValidationError(u'Nie możesz podać daty po %s' % str(self.instance.zlot.koniec))
        return od
    
    def clean_do(self):
        do = self.cleaned_data['do']
        if do is not None:
            if do < self.instance.zlot.start:
                raise ValidationError(u'Nie możesz podać daty przed %s' % str(self.instance.zlot.start))
            if do > self.instance.zlot.koniec:
                raise ValidationError(u'Nie możesz podać daty po %s' % str(self.instance.zlot.koniec))
        return do

    def clean_caly(self):
        caly = self.cleaned_data.get('caly', None)
        do = self.cleaned_data.get('do', None)
        od = self.cleaned_data.get('od', None)
        if not caly and not od and not do:
            raise ValidationError(u'Musisz wybrać jedną z opcji')
        return caly
    
    def clean(self):
        cleaned = self.cleaned_data
        caly = cleaned.get('caly')
        od = cleaned.get('od')
        do = cleaned.get('do')
        if od is not None and do is not None and caly is not None:
            if od == self.instance.zlot.start and do == self.instance.zlot.koniec and caly == 0:
                   self.cleaned_data['caly'] = 1;
        return cleaned
    
    class Meta:
        model = Uczestnictwo
        fields = ('caly','od','do', 'larp_uczestnictwo', 'larp_postac')


class NoweUczestnictwoForm(UczestnictwoForm):
    username = forms.CharField(required = True)
    password = forms.CharField(widget = forms.PasswordInput(), required = True)
    password2 = forms.CharField(widget = forms.PasswordInput(), required = True)
    email = forms.EmailField(required = True)
    larp_uczestnictwo = forms.ChoiceField(widget=forms.Select, choices = (('tak', 'Tak'), ('nie', 'Nie')))
    larp_postac = forms.ChoiceField(widget=forms.Select, choices = (('zadna', u'Wybierz'), ('gotowa', u'Wybiorę gotową postać'), ('wlasna',u'Chcę stworzyć własną postać')))
    
    def clean_email(self):
        try:
            Uczestnik.objects.get(email = self.cleaned_data['email'])
            raise ValidationError(u"Uczestnik o tym adresie email już istnieje")
        except Uczestnik.DoesNotExist:
            return self.cleaned_data['email']
    
    def clean_username(self):
        try:
            Uczestnik.objects.get(username = self.cleaned_data['username'])
            raise ValidationError(u"Uczestnik o tym nicku już istnieje")
        except Uczestnik.DoesNotExist:
            return self.cleaned_data['username']
    
    def clean_password2(self):
        p = p2 = ''
        p = self.cleaned_data.get('password', None)
        p2 = self.cleaned_data.get('password2', None)
        if p != p2:
            raise ValidationError(u'Oba hasła muszą być takie same')
        return self.cleaned_data['password2']
    
    
    class Meta:
        model = Uczestnictwo
        fields = ('username', 'password', 'password2', 'email', 'caly', 'od', 'do', 'larp_uczestnictwo', 'larp_postac')

class LoginForm(forms.Form):
    username = forms.CharField(label=u"Nick", required=True)
    password = forms.CharField(label=u"Hasło", widget=forms.PasswordInput(),required=True)
    
    def clean_username(self):
        try:
            Uczestnik.objects.get(username=self.cleaned_data['username'])
        except Uczestnik.DoesNotExist:
            raise ValidationError(u"Nie ma takiego użytkownika")
        return self.cleaned_data['username']
    
    def clean_password(self):
        try:
            u = Uczestnik.objects.get(username=self.cleaned_data['username'])
            if not u.check_password(self.cleaned_data['password']):
                raise ValidationError(u"Niepoprawne hasło")
        except Uczestnik.DoesNotExist:
            pass
        return self.cleaned_data['password']

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label=u"Nowe hasło", widget=forms.PasswordInput(),required=True)
    password_confirm = forms.CharField(label=u"Potwierdź nowe hasło", widget=forms.PasswordInput(),required=True)
    
    def clean(self):
        if self.cleaned_data['new_password'] == self.cleaned_data['password_confirm']:
            return self.cleaned_data
        raise ValidationError(u"Hasła nie są takie same")
        
class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(label=u"Stare hasło", widget=forms.PasswordInput(),required=True)
    new_password = forms.CharField(label=u"Nowe hasło", widget=forms.PasswordInput(),required=True)
    password_confirm = forms.CharField(label=u"Potwierdź nowe hasło", widget=forms.PasswordInput(),required=True)
    
    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        if cleaned_data['new_password'] == cleaned_data['password_confirm']:
            if self.instance.check_password(cleaned_data['old_password']): 
                return cleaned_data
            raise ValidationError(u"Stare hasło jest niepoprawne")
        raise ValidationError(u"Nowe hasła nie są takie same")
    
    class Meta:
        model = Uczestnik
        fields = ['old_password', 'new_password', 'password_confirm']

class AddWpisForm(forms.ModelForm):
    class Meta:
        model = Wpis
        fields = ['text',]