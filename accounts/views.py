from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext_lazy as _

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'registration/user-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        message = _('We sent an email to your account. Please, verify your email address')
        messages.success(self.request, message)
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = 'registration/user-login.html'

# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('')
