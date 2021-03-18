from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    #one to many relationship, we are connecting to the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #foreng key takes the id of the user that is making this todo and it saves the ID in this feild
    #in this way we are enabled to return specific information -> one-to many relationship
    
    #show the titles for the admin windows
    def __str__(self):
        return self.title
    
    
    
    