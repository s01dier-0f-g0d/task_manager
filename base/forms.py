from django import forms
from .models import Task, Priority

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name']
        widgets ={'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Priority Category'})}

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','priority','estimated_hours','progress']