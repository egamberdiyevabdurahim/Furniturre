from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = None
    email = forms.EmailField(required=True)
