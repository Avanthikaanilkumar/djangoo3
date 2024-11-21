from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse


# Create your views here.
from.forms import CustomUser1
def Cust(req):
    if req.method =='POST':
        form=CustomUser1(req.POST)
        if form.is_valid():
            form.save()
            return redirect('x')
    else:
        form=CustomUser1()
    return render(req,'register.html',{'formm':form})

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def user_login(req):
    if req.method == 'POST':
        username=req.POST.get('name')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('ad')
        else:
            messages.error(req,'invalid username')
    return render(req,'login.html')
@login_required
def home(req):
    return render(req,'home.html')
def user_logout(req):
    logout(req)
    messages.info(req,"You have been loggedout")
    return redirect('x')
@permission_required('apps.can_view_protected_page')
def protected_view(req):
    return render(req,'protected.html',{'userr':req.user})



def log_session(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        password=req.POST.get('password')
        user=user1.objects.filter(Name=name,password=password).first()
        if user is not None:
            req.session['user_id']=user.user_id
            req.session['Name']=user.Name
            return redirect('login')
        else:
            return render(req,'login.html')
    else:
        return render(req,'login.html')
    
def login_view(req):
    return render(req,'login1.html')

def login_session(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        password=req.POST.get('password')
        userr=new_model.objects.filter(new_name=name,password=password).first()
        if userr is not None:
            req.session['id']=userr.id
            req.session['name']=userr.new_name
            return redirect('ad')
        else:
            return render(req,'login.html')
    else:
        return render(req,'login.html')
    
@login_required
def admin_page(req):
    if req.user.groups.filter(name='admin').exists():
        b='Admin'
        return render(req,'admin.html',{'name':b})
    elif req.user.groups.filter(name='staff').exists():
        b='staff'
        return render(req,'admin.html',{'name':b})
    elif req.user.groups.filter(name='customer').exists():
        b='customer'
        return render(req,'admin.html',{'name':b})
    else:
        return HttpResponse('You do not have permissions to this page')
        
    
