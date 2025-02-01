from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todoapp.models import TODOO
from . import models
from django.contrib.auth import authenticate, login as auth_login, logout
from  django . shortcuts  import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        
        my_user = User.objects.create_user(username=emailid, email=emailid, password=pwd)
        my_user.save()
        
        return redirect('/login')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(emailid, pwd)

        userr = authenticate(request, username=emailid, password=pwd)
        if userr is not None:
            auth_login(request, userr)
            return redirect('/todo')
        else:
            return redirect('/login')
            
    return render(request, 'login.html')

def todo(request):
     if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.TODOO(title=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.TODOO.objects.filter(user=user).order_by('-date')
        return redirect('/todo',{'res':res})

     res=models.TODOO.objects.filter(user=request.user).order_by('-date')
     return render(request, 'home.html',{'res':res,})


def delete_todo(request,srno):
    print(srno)
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')

@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit.html', {'obj': obj})





def signout(request):
    logout(request)
    return redirect('/login')