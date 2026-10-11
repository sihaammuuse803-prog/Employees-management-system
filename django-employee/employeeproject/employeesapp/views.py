from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Employee
from .forms import SalaryForm
from .models import  Employee ,Department ,Position ,Attendance ,Salary



def dashboard(request):
    total_employees = Employee.objects.count()
    active_employees = Employee.objects.filter(status='Active').count()

    context = {
        'total_employees': total_employees,
        'active_employees': active_employees,
    }

    return render(request, 'dashboard.html', context)


def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'list.html', {
        'employees': employees
    })
def add_employee(request):
    return render(request, 'add_employee.html')

def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        department = request.POST['department']
        position = request.POST['position']
        date_joined = request.POST['date_joined']
        salary = request.POST['salary']

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            department=department,
            position=position,
            date_joined=date_joined,
            salary=salary
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')


def department_list(request):
    departments = Department.objects.all()

    return render(request, 'department.html', {
        'departments': departments
    })

def add_department(request):
    if request.method == 'POST':
        name = request.POST['name']

        Department.objects.create(
            name=name
        )

        return redirect('department_list')
    return render(request, 'add_department.html')
    

def position_list(request):
    positions = Position.objects.all()
    return render(request, 'position.html', {
        'positions': positions
    })  

def add_position(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            Position.objects.create(name=name)
            return redirect('position_list')

    return render(request, 'add_position.html')

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance.html', {
        'attendances': attendances
    })  


def add_attendance(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        date = request.POST.get('date')
        status = request.POST.get('status')

        Attendance.objects.create(
            employee_id=employee_id,
            date=date,
            status=status
        )

        return redirect('attendance_list')

    return render(request, 'add_attendance.html', {
        'employees': employees
    })
def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'salary.html', {
        'salaries': salaries
    })

def add_salary(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('payment_date')
        month = request.POST.get('month')

        Salary.objects.create(
            employee_id=employee_id,
            amount=amount,
            payment_date=payment_date,
            month=month
        )

        return redirect('salary_list')

    context = {
        'employees': employees,
    }

    return render(request, 'add_salary.html', context)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Halkan ayaa ku geeneysa dashboard-ka
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')