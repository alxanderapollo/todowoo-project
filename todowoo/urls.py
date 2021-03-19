
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Auth   
    path('signup/',views.signupuser, name ="signupuser"),
    path('logout/',views.logoutuser, name ="logoutuser"),
    path('login/',views.loginuser, name ="loginuser"),
    
    #todos
    path('current/', views.currenttodos, name ="currenttodos"),
    path('create/', views.createtodo, name ="createtodo"),
    path('todo/<int:todo_pk>', views.viewtodo, name ="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('completed/', views.completedtodos, name='completedtodos'),
    
    
    
    path('', views.home, name ='home'),
]
