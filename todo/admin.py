from django.contrib import admin
from .models import Todo

#allows us to customize the windows in admin
#read only
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)

# Register your models here.
