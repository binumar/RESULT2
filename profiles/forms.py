from django import forms
from django.contrib.auth.forms import UserCreationForm
from profiles.models import User, StudentProfile, TeacherProfile, FormMasterProfile
from django.forms import ModelForm

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-2 px-2 rounded-lg focus:outline-none focus:border-blue-500'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-2 px-2 rounded-lg focus:outline-none focus:border-blue-500'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full p-2 border rounded-lg focus:outline-none focus:border-blue-500'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full p-2 border rounded-lg focus:outline-none focus:border-blue-500'
    }))

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['full_name', 'subject']  

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'w-full py-2 px-2 rounded-lg focus:outline-none focus:border-blue-500 border m-4'
    }))

class FormMasterProfileForm(forms.ModelForm):
    class Meta:
        model = FormMasterProfile
        fields = ['full_name', 'level']  

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'w-full py-2 px-2 rounded-lg focus:outline-none focus:border-blue-500 border m-4'
    }))

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'level']  

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'w-full py-2 px-2 rounded-lg focus:outline-none focus:border-blue-500 border m-4'
    }))
