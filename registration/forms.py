from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]


# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'city', 'address', 'locality', 'phone_no','house_no', 'zip_code',]
        labels = {'house_no':'House no (Optional)','zip_code':'Zip code (Optional)'}
        widgets = {
            'house_no': forms.NumberInput(attrs={'required':False}),
            'zip_code':forms.NumberInput(attrs={'required':False}),
            }
