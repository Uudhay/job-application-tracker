from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_role', 'status', 'applied_date', 'notes']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),
            'job_role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job role'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'applied_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notes (optional)',
                'rows': 3
            }),
        }