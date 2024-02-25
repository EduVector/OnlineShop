from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate'}), required=True)
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'validate'}), required=True)
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'validate'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'validate'}), required=True)
    confirm_password = forms.CharField(widget=PasswordInput(attrs={'class': 'validate'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'confirm_password']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already exists!")
        
        return username
    
    def clean_confirm_password(self):
        data = self.cleaned_data

        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Password did not match!")
        
        return data['confirm_password']
    
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'validate'}), required=True)






    

            



