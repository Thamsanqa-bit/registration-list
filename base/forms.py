from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'postal_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'postal_code': 'Postal.Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['postal_code'].required = False