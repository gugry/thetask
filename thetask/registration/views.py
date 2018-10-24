# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import  login
from django.http import JsonResponse
from django.shortcuts import    render
from django.urls import reverse
from .forms import Reg_form
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def reg_form(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        if request.is_ajax():
            user = form.save()
            login(request, user)
            data = {
                'result': 'Успех!',
            }
            return JsonResponse(data)
        else:
            return HttpResponse('not Ajax')
    if request.is_ajax():
        return JsonResponse(form.errors, status=400)
    return render(request, 'registration/reg.html', {'form': form})



def usernamevalidate(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    # raw_pass = encode(password)
    user = User.objects.filter(username__iexact=username)[0]

    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
        'is_correct': User.check_password(user,password)
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)