from django import forms
from .models import Contact

# class for building new form for users
class NewContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'
