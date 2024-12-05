from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from health_assist.accounts.forms import EmployeeRegistrationForm, ProfileChangeForm
from health_assist.accounts.models import EmployeeProfile


class RegisterView(CreateView):
    form_class = EmployeeRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('health-home')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = EmployeeProfile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Ensure the view fetches the profile for the logged-in user
        return get_object_or_404(EmployeeProfile, user=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeProfile
    form_class = ProfileChangeForm
    template_name = 'accounts/profile-set-up.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        profile = EmployeeProfile.objects.get(user=self.request.user)
        return profile

