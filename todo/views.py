from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
# to generate the model to create a user object
from django.contrib.auth.models import User
from django.db import IntegrityError #checks to see if the user has already created an object that already exists in the DB
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
# Create your views here.

def home(request):
    return render(request,'todo/home.html')
    
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
                return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'That username has already been taken! Please choose a new user name. Try Again '})

                
        else:
             return render(request, 'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})
            #tell the user the passwords didnt match

def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    
     if request.method == 'GET':
            #passing in django user creation forms
        return render(request, 'todo/loginuser.html',{'form':AuthenticationForm()})
     else:
         #returns a a user object
        user =  authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #if the username did not match throw it doesnt exist error
        if user is None:
            return render(request, 'todo/loginuser.html',{'form':AuthenticationForm(),'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')

def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'todo/currenttodos.html',{'todos':todos})


def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk =todo_pk, user = request.user )
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request,'todo/viewtodo.html',{'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:  
            return render(request,'todo/viewtodo.html',{'todo':todo, 'form':form, 'error':"Bad info!"})  
        
 
        
    
 
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html',{'form':TodoForm()})
    else:
        try:
            #first get the information from the post request and connect with our form
            #pass in any informatin that is saved in POST
            form = TodoForm(request.POST)
            #create a new todo objext and dont put it in the data base yet
            newTodo = form.save(commit=False)
            #the object will get the user, so we are specifying only the user
            newTodo.user = request.user
            #now put it back into the data base
            newTodo.save()
            #return back to the page
            return redirect('currenttodos')
        except ValueError:
            return  render(request, 'todo/createtodo.html',{'form':TodoForm(), 'error':'Bad Data passed in'})
       

