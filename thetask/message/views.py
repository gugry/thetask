# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .forms import  MessageForm

@login_required
def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            response = saved
            return HttpResponse(response)
    else:
        form =MessageForm()
    return render(request, 'message/message.html', {'form': form})

