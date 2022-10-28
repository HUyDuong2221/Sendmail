from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
#message
from django.contrib import messages

# send mail
from .models import send_mail as mailmodel , read_mail, customer
from .forms import SendMailForm, CustomerForm
import email
import random
from django.conf import settings
from django.core.mail import send_mail
# nhận mail
import imaplib
import re
#search
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#firebase



# Create your views here.
#firebase


# tìm kiếm customer
@csrf_exempt
def search_customer(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        mail = customer.objects.filter(
            email__istartswith = search_str) | customer.objects.filter(
            name__icontains = search_str) | customer.objects.filter(phone__icontains = search_str)
        
        data = mail.values()
        return JsonResponse(list(data), safe = False)


@login_required(login_url='login')
def add_customer(request):
    ds = customer.objects.all()
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thêm mới thành công')
    return render(request, 'cus.html',{'form': form, 'ds': ds})

@login_required(login_url='login')
def edit_customer(request):
    
    return HttpResponse('aa')

@login_required(login_url='login')
def delete_customer(request):
    
    return HttpResponse('aa')


#Gửi Mail
@login_required(login_url='login')
def ds_mail(request):
    ds = mailmodel.objects.all()
    return render(request, 'listMail.html',{'ds':ds})

@login_required(login_url='login')
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
@login_required(login_url='login')
def ds_mail_nhan(request):
    dsn = read_mail.objects.all()
    return render(request, 'nhan.html',{'dsn':dsn})

@login_required(login_url='login')
def nhan_mail(request):
    username ="huyduong111.dn@gmail.com"
    app_password= "vfdxrsbrkbznlgma"
    gmail_host= 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(gmail_host)
    mail.login(username, app_password)
    mail.select("INBOX")
    
    _, selected_mails = mail.search(None, 'ALL')
    a = len(selected_mails[0].split())
    if a ==0:
        messages.success(request,'Không có thư mới')
        return redirect('ds_mail_n')
    
        
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
        mess2 = mess1.strip('<br>'+ '<div>')  
        sub1= sub[4:]  
        print(sub1)
        list_title = list(mailmodel.objects.values_list('title'))
        print(list_title)
        if sub1 != '':
            for i in list_title:
                
                b = str(sub1) in str(i) 
                print(b)
                if b is True:
                    save_mail = read_mail.objects.create(Subject = sub1, To = to, send_date= date, From = fro, Message=mess2)     
                    save_mail.save() 
    messages.success(request,'đã cập nhật thư mới')
    return redirect('ds_mail_n')   
    #messages.success(request,'đã cập nhật thư mới')
    #return redirect('ds_mail_n')
                #else:
                    #messages.success(request,'Không có thư phản hồi')
                    #return render(request, 'nhan.html',{'dsn': dsn})      


    
       
     
            
