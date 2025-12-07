from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
 
def home(request):
    return redirect('employee_list')
 
def employee_list(request):
    # TEMPORARY: Test with hardcoded data (no database query)
    hardcoded_employees = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'position': 'Manager', 'department': 'IT'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'position': 'Developer', 'department': 'IT'},
        {'id': 3, 'name': 'Bob Johnson', 'email': 'bob@example.com', 'position': 'Designer', 'department': 'Design'},
    ]
    # Use hardcoded data instead of database
    page_obj = None
    total_employees = len(hardcoded_employees)
    context = {
        'page_obj': None,
        'employees': hardcoded_employees,
        'total_employees': total_employees,
    }
    return render(request, 'employee_list.html', context)
 
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('employee_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form, 'title': 'Add Employee'})
 
    
def employee_update(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'employee_form.html', {'form': form, 'title': 'Edit Employee'})
 

def employee_delete(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')