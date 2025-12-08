from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Home redirects to employee list
def home(request):
    return redirect('employee_list')



# Authentication Views


def signup(request):
    if request.user.is_authenticated:
        return redirect('employee_list')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # creates user with hashed password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate and log in the new user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Account created successfully. Welcome {username}!")
                return redirect('employee_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('employee_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('employee_list')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')



# Employee CRUD Views


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@login_required
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


@login_required
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


@login_required
def employee_delete(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')
