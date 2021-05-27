from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, EmailValidator, MinLengthValidator
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError


class UserProfileInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8)])

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)  # default User contains these fields including first_name,last_name

    def save_user(self, form):
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        uemail = form.cleaned_data['email']
        user = User.objects.create_user(username=uname, password=upass, email=uemail)
        user.is_active = True
        user.save()


class UserProfileLoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
