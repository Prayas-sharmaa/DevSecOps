# storewebapp/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'role', 'shift')
    search_fields = ('name', 'contact', 'role')
