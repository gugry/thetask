# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate

from .forms import Reg_form
# from .forms import NameForm, Form_from_model


#
# def form_from_model(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:8+*7-+77
#         form = Reg_form(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             saved = form.save()
#             # response = request.POST['simple_name']
#             return HttpResponse('успешно')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = Reg_form()
#     return render(request, 'registration/reg.html', {'form': form})



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

        # return redirect('url_name', param1=value)
    # return direct_to_template(request, 'registration/reg.html', {'form': form})
    return render(request, 'registration/reg.html', {'form': form})

#
# def reg_form(request):
#     if request.method == 'POST':
#         form = Reg_form(request.POST)
#
#     else:
#         form = Reg_form()
#     if form.is_valid():
#         if request.is_ajax():
#             user = form.save()
#             login(request, user)
#             data = {
#                 'redirect': reverse('index'),
#             }
#             return JsonResponse(data)
#         else:
#             return HttpResponse('not Ajax')
#     if request.is_ajax():
#         return JsonResponse(form.errors, status=400)
#     return render(request, 'registration/reg.html', {'form': form})


