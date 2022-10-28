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
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('name', 'phone','email',)
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__( *args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})