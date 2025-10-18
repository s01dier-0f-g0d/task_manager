from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from .models import Task

from base.forms import TaskForm
from django.contrib import messages
from django.db.models import Q

def home(request):
    total = Task.objects.count()
    completed = Task.objects.filter(progress=100).count()
    return render(request, 'home.html', {'total': total, 'completed': completed})



def display(request):
    search = request.GET.get('q')
    if search:
        data=Task.objects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(priority__icontains=search) |
            Q(estimated_hours__icontains=search) |
            Q(progress__icontains=search) 
        )
    else:
        data = Task.objects.all()
        data=data.order_by('-id')
    return render(request,'display.html',{'data':data})

def update(request,key):
    data = get_object_or_404(Task, id=key)
    form = TaskForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,'Task has been Modified')
        return redirect('display')
    return render(request,'update.html',{'form':form, 'data':data})

def deleteTask(request,key):
    data=get_object_or_404(Task, id=key)
    if request.method =='POST':
        data.delete()
        messages.success(request,'Task Deleted')
        return redirect('display')
    return render(request,'deleteTask.html',{'data':data})

def specific(request,key):
    data = get_object_or_404(Task, id=key)
    return render(request, 'specific.html', {'data': data})

def create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Task created successfully')
        return redirect('home')
    return render(request,'create.html',{'form':form})