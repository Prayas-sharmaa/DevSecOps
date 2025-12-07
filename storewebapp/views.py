from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
 
# Create your views here.
 
def home(request):
    return redirect('employee_list')
 
# To perform CRUD operations
 
def employee_list(request):
    # Get all employees (query is not executed yet - it's lazy)
    employees_query = Employee.objects.all().order_by('-id')
    # Create paginator - show 25 employees per page
    paginator = Paginator(employees_query, 25)
    # Get the page number from URL (e.g., ?page=2)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'employees': page_obj.object_list,  # Current page employees
        'total_employees': paginator.count,
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