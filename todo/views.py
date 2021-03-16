from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def signupuser(request):
    #passing in django user creation forms
    return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})