from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class LoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:home')
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    next_page = 'core:home'