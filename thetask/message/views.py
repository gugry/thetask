from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import  MessageForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request, saved=None):
    superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            mail = EmailMessage('Сообщение с сайта', new_message.message_text, '',
                settings.ADMINS, [''],
                reply_to=[new_message.message_email],
            )
            try:
                new_message.message_status = mail.send()
                context = {'result': 'Письмо отправлено'}
            except BaseException as err:
                print(err)
                new_message.message_status = 0
                context = {'result': "Проблемы при отправке"}
            new_message.save()
            return JsonResponse(context)
    else:
        form = MessageForm()
    return render(request, 'message/message.html', {'form': form})



def admin_emails(request):
    out = { 'ADMINS': settings.ADMINS }


    return HttpResponse(out)



