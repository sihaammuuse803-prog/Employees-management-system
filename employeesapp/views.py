#from django.shortcuts import render
#from .models import Employee

#def employee_list(request):
 #   employees = Employee.objects.all()
  #
  #  return render(request, 'employee_list.html', {'employees': employees})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import render
def Dashboard(request):
    return render(request,'Dashboard.html')

def employee_list(request):
    q = request.GET.get('q', '')
    employees = Employee.objects.all()
    if q:
        employees = employees.filter(first_name__icontains=q) | employees.filter(last_name__icontains=q)
    return render(request, 'employee_list.html', {'employees': employees, 'q': q})

def employee_add(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form': form, 'title': 'Ku dar shaqaale'})

def employee_edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'form': form, 'title': 'Wax ka bedel'})

def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'emp': emp})

