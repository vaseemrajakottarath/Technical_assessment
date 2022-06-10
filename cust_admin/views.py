from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# from AcmeSupport.user import forms
from user.models import User,Department
from user.forms import RegistrationForms
from .forms import TicketForm

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        admin = auth.authenticate(email=email, password=password)
        if admin:
            if admin.role == 'Admin':
                auth.login(request, admin)
                return redirect('admin_home')
        messages.error(request, 'invalid credentials')       
    return render(request, 'login.html')


@login_required(redirect_field_name=None, login_url='admin_login')
def home(request):
    users = User.objects.all().exclude(role='Admin')
    context = {
        'users': users
    }
    return render(request, 'home.html', context)

def logout(request):
    auth.logout(request)
    return redirect('admin_login')

def create_user(request):
    if request.method=='POST':
        form=RegistrationForms(request.POST)
        print(form.is_valid())
        print(form.errors)
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists')
        elif User.objects.filter(phone_number=request.POST['phone_number']).exists():
            messages.error(request, 'Phone number already exists')

        elif form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            password=form.cleaned_data['password']
            department=form.cleaned_data['department']


            user=User.objects.create_user(name=name,email=email,phone_number=phone_number,password=password,department=department)
            user.save()
            messages.success(request,'Registration Successful.')
            return redirect('admin_home')
    
    form=RegistrationForms()
    context={
        'form':form
    }
    return render(request,'create_user.html',context)


def department(request):
    departments=Department.objects.all()
    context={
        'departments':departments
    }
    return render(request,'department.html',context)

def add_department(request):
    if request.method=='POST':
        department_name=request.POST['department_name']
        description=request.POST['description']
        if Department.objects.filter(name=department_name).exists():
            print("existing department")
            return redirect('add_department')
        else:
            add_department=Department.objects.create(name=department_name,description=description)
            add_department.save()
            return redirect('department')
    return render(request,'add_department.html')

def update_department(request,pk):
    department=Department.objects.get(id=pk)
    context={'department':department}
    if request.method=='POST':
        department_name=request.POST['department_name']
        description=request.POST['description']

        department.name=department_name
        department.description=description
        department.save()
        return redirect('department')

    return render(request,'update_department.html',context)

def delete_department(request,pk):
    department=Department.objects.get(id=pk)
    user=User.objects.filter(department=department)
    if user:
        messages.error(request,"This department is associated with a user")
    else:
        department.delete()
        messages.success(request,"Department Deleted")
    return redirect('department')

def ticket(request):
    return render(request,'ticket.html')

def create_ticket(request):
    form=TicketForm()
    context={'form':form}
    return render(request,'create_ticket.html',context)