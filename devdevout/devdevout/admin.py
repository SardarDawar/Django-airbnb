from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class User_DataAdmin(admin.ModelAdmin):
    list_display = ['title', 'Destination', 'Max_Budget']


    
    
admin.site.register(User_Data, User_DataAdmin)
admin.site.register(Trip_Content)






