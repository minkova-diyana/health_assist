from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from health_assist.accounts.forms import EmployeeRegistrationForm, ProfileChangeForm, EmployeeUserChangeForm, \
    EmployeePasswordChangeForm
from health_assist.accounts.models import EmployeeProfile, HnfUserModel


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


@login_required
def update_email(request, pk):
    user = get_object_or_404(HnfUserModel, pk=pk)
    if request.method == 'POST':
        user_form = EmployeeUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

    else:

        user_form = EmployeeUserChangeForm(instance=request.user)
        context = {
            'user_form': user_form,
        }
        return render(request, 'accounts/email-update.html', context)

class UpdatePasswordView(PasswordChangeView):
    form_class = EmployeePasswordChangeForm
    model = get_user_model()
    template_name = 'accounts/password-update.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user'] = user
        return context
