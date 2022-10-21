from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
#message
from django.contrib import messages
from flask import url_for
# send mail
from .models import send_mail as mailmodel , read_mail
from .forms import SendMailForm
import email
import random
from django.conf import settings
from django.core.mail import send_mail
# nhận mail
import imaplib
import re

# Create your views here.

#Gửi Mail
def ds_mail(request):
    ds = mailmodel.objects.all()
    return render(request, 'listMail.html',{'ds':ds})

def send_gmail(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        
        if form.is_valid():
            email = request.POST['email']
            title1 = request.POST['title']
            name = request.POST['name']
            content1 = request.POST['content']
            room_type = request.POST['room_type']
            check_in = request.POST['check_in']
            check_out = request.POST['check_out']
            
            content = 'Dear ' +name +',\n' + 'After checking room availability, Danafun company sends bk:' + content1 + '\n check in: ' + check_in + '\n check in: ' + check_out+'\n room type: '+ room_type
            random_num = random.randrange(100, 999)
            title = title1 + str(random_num)
            send_mail(title, content, settings.EMAIL_HOST_USER, [email], fail_silently=False )
            
            save_form = mailmodel.objects.create(title = title, email = email, content= content)
            save_form.save()
            messages.success(request,'Gửi mail thành công')
        else:
            messages.success(request,'Gửi mail thất bại (nhập sai)')
    else: 
        form = SendMailForm()
        
    return render(request, 'send.html', {'form': form })

#Nhận Mail
def ds_mail_nhan(request):
    dsn = read_mail.objects.all()
    return render(request, 'nhan.html',{'dsn':dsn})

def nhan_mail(request):
    dsn = read_mail.objects.all()
    username ="huyduong111.dn@gmail.com"
    app_password= "vfdxrsbrkbznlgma"
    gmail_host= 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(gmail_host)
    mail.login(username, app_password)
    mail.select("INBOX")
    
    _, selected_mails = mail.search(None, 'UNSEEN')
    a = len(selected_mails[0].split())
    if a >0 :
        for num in selected_mails[0].split():
            _, data = mail.fetch(num , '(RFC822)')
            _, bytes_data = data[0]
            email_message = email.message_from_bytes(bytes_data)
            
            #Lấy thông tin người gửi
            sub = email_message['subject']
            fro = email_message['from']
            to = email_message['to']
            date = email_message['date']
            
            #lấy Tin nhắn
            for part in email_message.walk():
                if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                    message = part.get_payload(decode=True)
                    mess = message.decode()
            stt = mess.find('</div>')
            mess1 = mess[15:stt]
            mess2 = mess1.strip('<br>')  
            sub1= sub[3:]  
       
            save_mail = read_mail.objects.create(Subject = sub1, To = to, send_date= date, From = fro, Message=mess2)     
            save_mail.save()            
        messages.success(request,'đã cập nhật thư mới')
        return redirect('ds_mail_n')
                #else:
                    #messages.success(request,'Không có thư phản hồi')
                    #return render(request, 'nhan.html',{'dsn': dsn})         
    elif a ==0:
        #return HttpResponse('Không có thư mới')
        messages.success(request,'Không có thư mới')
        return redirect('ds_mail_n')
             
        
                #else:
                    #return HttpResponse('Không có thư phản hồi')
            
     
                    
                    
            
                    
            
