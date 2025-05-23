from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=155,required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
