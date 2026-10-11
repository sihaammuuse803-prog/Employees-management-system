from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_joined = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Active')


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name   

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, default='Present')

    def _str_(self):
        return f"{self.employee} - {self.date}"


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salaries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    month = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.employee} - {self.amount}"