from django import forms
from .models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['message_status', 'message_text']