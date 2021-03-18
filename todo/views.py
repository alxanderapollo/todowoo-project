from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
# to generate the model to create a user object
from django.contrib.auth.models import User
from django.db import IntegrityError #checks to see if the user has already created an object that already exists in the DB
from django.contrib.auth import login 
# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        #passing in django user creation forms
        return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #create new user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save() #inserts and saves it into the DATABASE
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError :
                return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'That username has already been taken! Please choose a new user name '})

                
        else:
             return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})
            #tell the user the passwords didnt match

def currenttodos(request):
     return render(request,'todo/currenttodos.html')

