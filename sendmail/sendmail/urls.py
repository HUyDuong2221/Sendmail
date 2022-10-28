"""sendmail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from send_gmail import views
from login_user import views as view_login
from notification import views as noti_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    #email
    path('', views.ds_mail, name='ds_mail' ),
    path('sendmail/', views.send_gmail, name='send_mail' ),
    
    path('mail/', views.ds_mail_nhan, name='ds_mail_n'),
    path('mail/xem', views.nhan_mail, name='d'),
    
    path('search_customer', views.search_customer, name='search' ),
    path('add/', views.add_customer, name='add_customer' ),
    path('edit/', views.edit_customer, name='edit_customer' ),
    #Login
    path('login/', view_login.login_user, name='login'),
    path('register/', view_login.register, name='register'),
    path('logout/', view_login.logoutUser, name='logout' ),
    #nothipication
    path('index/', noti_view.main, name='index' ),
    path('index2/', noti_view.showFirebaseJS, name='' ),
    
]
