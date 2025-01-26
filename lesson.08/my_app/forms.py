from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'phone_number', 'platform_type', 'legal_entity', 'problem_description',
            'problem_location', 'problem_type', 'task_date'
        ]
        widgets = {
            'task_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }