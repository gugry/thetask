# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import  login
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import Reg_form


def reg_form(request):
    form = Reg_form(request.POST or None)
    if form.is_valid():
        if request.is_ajax():
            user = form.save()
            login(request, user)
            data = {
                'redirect': reverse('index'),
            }
            return JsonResponse(data)
        else:
            return HttpResponse('not Ajax')
    if request.is_ajax():
        return JsonResponse(form.errors, status=400)
    return render(request, 'registration/reg.html', {'form': form})



