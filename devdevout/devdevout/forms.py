from django import forms
from django.forms import ModelForm

from .models import *

class trip_contentform(ModelForm):
    class Meta:
        model=Trip_Content
        exclude=['initial_data']

class user_dataform(ModelForm):
    class Meta:
        model=User_Data
        fields='__all__'


# class blogform(ModelForm):
#     class Meta:
#         model=Blog
#         fields = '__all__'

