from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField




class User_Data(models.Model):
    Destination              =       models.CharField(max_length=100)
    Max_Budget               =       models.IntegerField()
    Number_of_days           =       models.IntegerField()
    title                    =       models.TextField()
    Social_media_links       =       models.TextField(blank=True)
    created_at               =       models.DateTimeField(auto_now=True)
    updated                  =       models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at","-updated"]
        verbose_name_plural= 'User Data'
    def __str__(self):
        return self.title




class Trip_Content(models.Model):
    initial_data    = models.ForeignKey(User_Data,on_delete=models.CASCADE)
    description =       RichTextUploadingField()
    created_at  =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now=True)


  
    
    class Meta:
        ordering = ["-created_at","-updated"]
        verbose_name_plural= 'Trip Content'



    

