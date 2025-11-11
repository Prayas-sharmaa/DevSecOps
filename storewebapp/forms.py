from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm): # ModelForm (special form class ) for creating/Updating employees
    class Meta: # internal configuration for the ModelForm
        model = Employee # for which model the form is for
        fields = ['name', 'contact', 'role', 'shift'] # whih field should appear in form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Staff Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Staff role'}),
            'shift': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Shift Name'}),
        }