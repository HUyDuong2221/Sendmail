from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('ds_mail')
        else:
            messages.success(request, 'Tài khoản hoặc mật khẩu không đúng')
    return render(request, 'login.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Đăng ký thành công')
        
    return render(request, 'register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')