from django.contrib import admin

# Register your models here.
from myapp.models import studentModel

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password']
    
    
admin.site.register(studentModel, studentAdmin)