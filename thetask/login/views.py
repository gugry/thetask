# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                # 'pk': self.object.pk,
                'redirect': response.url,
            }
            return JsonResponse(data)
        else:
            return response

class AjaxLogin(AjaxableResponseMixin, LoginView):
    template_name = 'login/0login.html'


# Create your views here.
