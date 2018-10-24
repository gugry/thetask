# from .models import models, SimpleModel
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
#
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
#
# class Form_from_model(forms.ModelForm):
#     class Meta:
#         model = SimpleModel
#         fields = ['simple_name', 'simple_text', 'simple_number']

class Reg_form(UserCreationForm):
    class Meta:
        model =  User
        fields = ("username", "password1", "password2")

