from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from health_assist.accounts.models import EmployeeProfile
from health_assist.web_pages.forms import ContactForm
from health_assist.web_pages.models import Information
from health_assist.web_pages.signals import contact_form_submitted


# Create your views here.
def home_page(request):
    insurances = Information.objects.filter(pages__name='insurances')
    general = 'No insurances added'
    health = 'No insurances added'
    if insurances:
        general = insurances.filter(type_insurance='general')[:3]
        health = insurances.filter(type_insurance='health')[:3]
    context = {
        'general': general,
        'health': health
    }
    return render(request, 'common/index.html', context)


class HealthHomeView(TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:

                return ['common/index.html']
            return ['accounts/home-login.html']
        return ['health_assist/health-home.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.is_authenticated and  not self.request.user.is_staff:
            profile = get_object_or_404(EmployeeProfile, user=self.request.user)
            context['profile'] = profile
            return context


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        contact_form_submitted.send(
            sender=ContactForm,
            **form.cleaned_data
        )
        return redirect('contact')
    context = {'form': form}
    return render(request, 'health_assist/health-contact.html', context)
