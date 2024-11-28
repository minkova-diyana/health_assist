from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from health_assist.accounts.forms import EmployeeRegistrationForm


class RegisterView(CreateView):
    form_class = EmployeeRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('health-home')
