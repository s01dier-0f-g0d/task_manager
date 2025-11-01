from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from .models import Task,Priority
from django.utils import timezone
from base.forms import TaskForm,PriorityForm
from django.contrib import messages
from django.db.models import Q

# Priority:
#Create Priority
def create_priority(request):
    form= PriorityForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Priority Created Successfully')
        return redirect('displayprior')
    return render(request, 'create_priority.html', {'form': form})

#Read Priority
def read_priority(request):
    search=request.GET.get('q')
    if search:
        data=Priority.objects.filter(
            Q(name__icontains=search)
        )
    else:
        data=Priority.objects.all()
    return render(request, 'read_priority.html',{'data':data, 'search':search})

#Update Priority
def update_priority(request, key):
    data = get_object_or_404(Priority, id=key)
    if request.method=='POST':  
        form = PriorityForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Priority Updated Successfully')
            return redirect('displayprior')
    else:
        form=PriorityForm(instance=data)
    return render(request,'update_priority.html',{'form': form})

#Delete Priority
def delete_priority(request, key):
    data = get_object_or_404(Priority, id=key)
    if request.method == 'POST':
        data.delete()
        messages.success(request,'Priority Deleted Successfully')
        return redirect('displayprior')
    return render(request, 'delete_priority.html', {'data': data})

# Task: 
def home(request):
    return render(request,'home.html')

def create(request):
    form= TaskForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'Task Created Successfully')
        return redirect('display')
    return render(request, 'create.html', {'form': form})


def display(request):
    search=request.GET.get('q')
    if search:
        data= Task.objects.filter(
            Q(title__icontains=search)|
            Q(desc__icontains=search)|
            Q(genre__icontains=search) 
        )
    else:
        data=Task.objects.filter(is_completed=False)
    return render(request,'display.html',{'data':data})

def specific(request,key):
    data = get_object_or_404(Task,id = key)
    return render(request,'specific.html',{'data':data})
#UPDATE
def update(request, key):
    data = get_object_or_404(Task, id=key)
    if request.method=='POST':
        form = TaskForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Task Updated Successfully')
            return redirect('display')
    else:
        form = TaskForm(instance=data)
    return render(request,'update.html',{'form': form})

#DELETE
def delete(request, key):
    data = get_object_or_404(Task, id=key)
    if request.method == 'POST':
        data.is_completed=True #data.delete() deletes data permanently
        data.completed_at=timezone.now()
        data.save()
        messages.success(request,'Task Completed Successfully')
        return redirect('display')
    return render(request, 'deleteTask.html', {'data': data})

#History
def history(request):
    search=request.GET.get('q')
    if search:
        data= Task.objects.filter(
            Q(title__icontains=search)|
            Q(description__icontains=search)|
            Q(progress__icontains=search)|
            Q(priority__icontains=search) 
        )
    else:
        data=Task.objects.filter(is_completed=True)
    return render(request,'history.html',{'data':data})

#Restore
def restore(request, key):
    data=get_object_or_404(Task, id=key, is_completed=True)
    if request.method=='POST':
        data.is_completed=False
        data.completed_at=None
        data.save()
        messages.success(request, "Task Restored Successfully")
        return redirect('history')
    return render(request, 'restore.html', {'data':data})