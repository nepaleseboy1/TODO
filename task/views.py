from multiprocessing import context
import pkgutil
from django.shortcuts import render,redirect 
from .models import *
from django.http import HttpResponse

from .forms import *



# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")  


    context = {'tasks': tasks , 'form': form} 
    

    return render(request,'base.html', context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)    #to use the same instance of the items 
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}

    return render(request,'update_task.html', context)  

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)    #to retrive the items by their id 

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item }
    return render(request,'delete.html', context)
    