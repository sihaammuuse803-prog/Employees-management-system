from .models import Salary
from django import forms

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'