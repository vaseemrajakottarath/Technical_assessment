import re
from django.contrib import messages,auth
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .backends import CustomAuthenticationBackend
from .forms import RegistrationForms
from .models import Department, User

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        
        user=CustomAuthenticationBackend.authenticate(email,password)
        print(user)
        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
    
    return render(request,'login.html') 

@login_required(redirect_field_name=None, login_url='user_login')
def home(request):
    return render(request,'user_home.html')
