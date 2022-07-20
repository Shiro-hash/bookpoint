from pyexpat import model
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AccountModel


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = AccountModel
        fields = ('email', 'username', 'password1', 'password2')


class UserEditForm(UserChangeForm):

    class Meta:
        model = AccountModel
        fields = ('email', 'username')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = AccountModel
        fields = ('email', 'password')

        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(AccountAuthenticationForm, self).__init___(*args, **kwargs)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
