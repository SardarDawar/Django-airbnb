from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *


def home(request):
    return render(request,'home.html',{})

def triplist(request):
    test=User_Data.objects.all()
    
    context={
        'test':test
    }
    return render(request,'list.html',context)

def tripdetail(request,id):
    data=User_Data.objects.get(id=id)
    desc=Trip_Content.objects.get(initial_data=data)
    print(desc.description)
    context={
        'data':data,
        'desc':desc,
    }
    return render(request,'tripdetail.html',context)


def  trip_content(request):
    test=User_Data.objects.all()
    for i in range(0,len(test)):
        k=test[i]
   
    form=trip_contentform()
    if request.method == 'POST':
        form=trip_contentform(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.initial_data=k
            new.save()
            form.save()
            return redirect('triplist')

    context={
        'form':form
    }
    return render(request,'tripcontent.html',context)

def  user_data(request):
    form=user_dataform()
    if request.method == 'POST':
        form=user_dataform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip')
    context={
        'form':form
    }
    return render(request,'userdata.html',context)

def myView(request, param):
    if not param:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    return render_to_response('404.html')


def myView1(request, param):
    if not param:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    return render_to_response('500.html')



