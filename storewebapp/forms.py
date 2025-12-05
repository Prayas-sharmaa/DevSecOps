# storewebapp/forms.py
from django import forms
from .models import Employee
import re

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'role', 'shift']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Staff Name',
                'required': True
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '10-digit Contact Number',
                'pattern': '^[0-9]{10}$',
                'title': 'Enter a valid 10-digit number',
                'required': True
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Role Name',
                'required': True
            }),
            'shift': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Morning / Evening / Night',
                'required': True
            }),
        }

# For Server Side Validations

    def clean_name(self): # For Name Validation
        name = self.cleaned_data.get("name")

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")

        if not re.match(r"^[A-Za-z ]+$", name):
            raise forms.ValidationError("Name must contain only letters and spaces.")

        return name

    def clean_contact(self): # For Contact validation
        contact = str(self.cleaned_data.get("contact"))

        if not re.match(r"^\d{10}$", contact):
            raise forms.ValidationError("Contact number must be exactly 10 digits.")

        return contact

    def clean_role(self): # For Role Validation
        role = self.cleaned_data.get("role")

        allowed_roles = ["Manager", "Cashier", "Staff", "Security"]
        if role not in allowed_roles:
            raise forms.ValidationError(f"Role must be one of: {', '.join(allowed_roles)}")

        return role

    def clean_shift(self): # For Shift Validation
        shift = self.cleaned_data.get("shift")

        allowed_shifts = ["Morning", "Evening", "Night"]

        if shift not in allowed_shifts:
            raise forms.ValidationError(f"Shift must be one of: {', '.join(allowed_shifts)}")

        return shift

# Cross Field Validation

    def clean(self):
        cleaned = super().clean()
        role = cleaned.get("role")
        shift = cleaned.get("shift")

        if role == "Manager" and shift != "Morning":
            raise forms.ValidationError("Managers must work the Morning shift.")

        return cleaned
