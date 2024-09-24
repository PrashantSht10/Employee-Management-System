from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.contrib import messages
from .forms import SignupForm, LoginForm

def signup_view(request):
    """View for user signup."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'employees/signup.html', {'form': form})

def login_view(request):
    """View for user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_form')  # Redirect to the main page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'employees/login.html', {'form': form})

def logout_view(request):
    """View for user logout."""
    logout(request)
    return redirect('login')

# Function to handle the display of the form and search functionality
def employee_form(request):
    if request.method == 'POST' and 'searchdata' in request.POST:
        search = request.POST['search']
        try:
            result = Employee.objects.get(eid=search)
        except Employee.DoesNotExist:
            result = None
        return render(request, 'employees/employee_form.html', {'result': result})

    return render(request, 'employees/employee_form.html')

# Function to handle creating and saving new employees
def save_employee(request):
    if request.method == 'POST' and 'save' in request.POST:
        name = request.POST['ename']
        gender = request.POST['gender']
        pno = request.POST['pno']
        department = request.POST['dept']
        address = request.POST['add']

        if name == "" or not name.replace(" ", "").isalpha():
            messages.error(request, 'Name field is empty or incorrect')
        elif pno == "" or not pno.isdigit():
            messages.error(request, 'Phone Number field is empty or incorrect')
        elif department == "" or not department.replace(" ", "").isalpha():
            messages.error(request, 'Department field is empty or incorrect')
        elif address == "":
            messages.error(request, 'Address field is empty or incorrect')
        else:
            employee = Employee(ename=name, gender=gender, phone_no=pno, department=department, address=address)
            employee.save()
            messages.success(request, 'Data is saved into Database')
        return redirect('employee_form')

# Function to handle deleting employees
def delete_employee(request):
    if request.method == 'POST' and 'delete' in request.POST:
        eid = request.POST['search']
        try:
            employee = Employee.objects.get(eid=eid)
            employee.delete()
            messages.success(request, 'Record deleted')
        except Employee.DoesNotExist:
            messages.error(request, 'Failed to delete')
        return redirect('employee_form')

# Function to handle updating employees
def update_employee(request):
    if request.method == 'POST' and 'update' in request.POST:
        eid = request.POST['search']
        name = request.POST['ename']
        gender = request.POST['gender']
        pno = request.POST['pno']
        department = request.POST['dept']
        address = request.POST['add']

        try:
            employee = Employee.objects.get(eid=eid)
            employee.ename = name
            employee.gender = gender
            employee.phone_no = pno
            employee.department = department
            employee.address = address
            employee.save()
            messages.success(request, 'Record updated')
        except Employee.DoesNotExist:
            messages.error(request, 'Failed to update')
        return redirect('employee_form')

