from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'email', 'age',
            'date_of_birth', 'gender', 'address', 'interest'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=Student._meta.get_field('gender').choices),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter complete address'}),
        }