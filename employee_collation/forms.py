from django import forms
from .models import Employee


class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'date_of_birth','date_of_employment','salary','position','supervisor' )
        labels = {
            'first_name':'First Name',
            'last_name' : 'Last Name'
        }
        widgets = {
            'date_of_birth': DateInput(), 
            'date_of_employment': DateInput()
        }
    def __init__(self, *arg, **kwargs):
        super(EmployeeForm,self).__init__(*arg, **kwargs)
        self.fields['position'].empty_label = "Select"