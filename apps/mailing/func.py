# -*- coding:utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from zapisy.forms import *
from zapisy.models import *
from django.conf import settings

def piszDoRekrutera(form):
    plemie = form.cleaned_data['plemie']
    text = u"""
    """
    SendEmail('noreply@arda.org.pl',plemie.rekruter_mail,u'Nowe zgłoszenie na Zlot Arda',text.encode('utf-8'))
    return True

def piszDoRekruta(form):
    plemie = form.cleaned_data['plemie']
    text = u"""
	"""
	SendEmail('ivellios@arda.org.pl',plemie.rekruter_mail,u'Raport z liczebności twojego plemienia',text.encode('utf-8'))
    return True



import smtplib
from email.MIMEText import MIMEText

def SendEmail(sender,recipient,subject,message,msgType=''):
    """
    Sends either a log file or a string message in email to
    recipient.
    Uses Google smtp server to send the mail.

    CHANGELOG:
    2006-12-7: Set sender, recipient, subject as input variables

    ---------------------------------------------------------------------------------------------
    Inputs:
    msgType: If 'log', message is path to log file that is to be
    written into email body
    sender: Senders email addy
    recipient: Who we want to send to
    subject: Email subject line
    message: Message body of email

    ---------------------------------------------------------------------------------------------
    """
    # determine msg type
    if msgType == 'log':
	# Send log file in email
        fp = open(message, 'rb')
        # Create a text/plain message
        # Read contents of log file into memory
        msg = MIMEText(fp.read())
        fp.close()
    else:
	# If not a log file, just create a text/plain message
        msg = MIMEText(message)

    # User/pwd
    me = settings.MAIL_ACCOUNT
    pwd = settings.MAIL_PASSWORD

    # Build the email
    fromAddr = sender
    toAddr = recipient
    msg['Subject'] = subject
    msg['From'] = fromAddr
    msg['To'] = toAddr

    # Set up and connect to smtp server
    server = smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(me, pwd)
    # Send the email
    server.sendmail(fromAddr, toAddr, msg.as_string())
    server.close()
