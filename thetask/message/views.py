# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .forms import  MessageForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

@login_required
def index(request, saved=None):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            mail = EmailMessage(
                'Сообщение с сайта',
                 new_message.message_text,
                '',
                settings.ADMINS,
                [''],
                reply_to=[new_message.message_email],
            )
            mail_count = mail.send()
            new_message.message_status =  mail_count
            new_message.save()
            return HttpResponse(mail_count)
    else:
        form = MessageForm()
    return render(request, 'message/message.html', {'form': form})



def admin_emails(request):
    out = { 'ADMINS': settings.ADMINS }


    return HttpResponse(out)



