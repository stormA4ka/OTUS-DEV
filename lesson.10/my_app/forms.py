from django import forms
from .models import Task, Users


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "phone_number",
            "platform_type",
            "legal_entity",
            "problem_description",
            "problem_location",
            "problem_type",
            "task_date",
        ]
        widgets = {
            "task_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["phone_number", "first_name", "last_name"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if len(phone_number) != 11 or not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять из 11 цифр.")
        return phone_number
