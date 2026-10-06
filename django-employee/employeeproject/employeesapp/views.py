from django.shortcuts import render , redirect
from .models import Employee
from .models import Department


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

    #commit 2