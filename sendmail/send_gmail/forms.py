import email
from django import forms
from .models import *

class SendMailForm(forms.ModelForm):
    class Meta:
        model = send_mail
        fields = ('title', 'email','send_date','content',)
        
class ReadMailForm(forms.ModelForm):
    class Meta:
        model = read_mail
        fields = ('Subject', 'To', 'send_date','From', 'Message',)