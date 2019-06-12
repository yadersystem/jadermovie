#import shortuuid
#from django.contrib.auth.views import PasswordChangeForm
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import Actor,Director,MovieRaiting,Movie, User
#from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            #'is_active',
            'date_joined',
        ]

        labels = {
            'username':'Username',
            'password':'Password',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            #'is_active':'Active',
            'date_joined':'Date',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','autofoco':'True'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            #'is_active':forms.CheckboxInput(attrs={'class':'forms-control'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'forms-control'}),
        }