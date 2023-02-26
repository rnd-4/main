from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={
                'type' : "username",
                'id' : "typeUsernameX",
                'class': "form-control form-control-lg"}))
    email = forms.CharField(widget= forms.TextInput(attrs={
                'type': "email",
                'id': "typeEmailX",
                'class': "form-control form-control-lg"}))
    password1 = forms.CharField(widget= forms.TextInput(attrs={
                'type': "password",
                'id': "typePassword1",
                'class': "form-control form-control-lg"}))
    password2 = forms.CharField(widget= forms.TextInput(attrs={
                'type': "password",
                'id': "typePassword2",
                'class': "form-control form-control-lg"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={
                'type': "username",
                'id': "typeUsernameX",
                'class': "form-control form-control-lg"}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': "password",
        'id': "typePasswordX",
        'class': "form-control form-control-lg"}))

    class Meta:
        model = User
        fields = ['username', 'password']