from django.contrib import admin
from  .models import *

# Register your models here.

@admin.register(send_mail)
class SendMailmodel(admin.ModelAdmin):
    list_filter = ('title', 'email', 'send_date', 'content')
    list_display = ('title', 'email', 'send_date', 'content')
    
@admin.register(read_mail)
class ReadMailmodel(admin.ModelAdmin):
    list_filter = ('Subject', 'To', 'send_date','From', 'Message')
    list_display = ('Subject', 'To', 'send_date','From', 'Message')
    
@admin.register(customer)
class Customermodel(admin.ModelAdmin):
    list_filter = ('name', 'phone','email')
    list_display = ('name', 'phone','email')