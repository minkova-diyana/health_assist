from django.views.generic import ListView, DetailView

from health_assist.accounts.models import EmployeeProfile
from health_assist.packages.models import CompanyPackages, UnderPackages


class UserPackage(ListView):
    model = UnderPackages
    template_name = 'accounts/account-insurance-package.html'
    context_object_name = 'company_packages'

    def get_queryset(self):
        profile = EmployeeProfile.objects.get(user=self.request.user)
        company = profile.company
        return UnderPackages.objects.filter(company=company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = EmployeeProfile.objects.get(user=self.request.user)
        context['profile'] = profile
        context['global_packages'] = CompanyPackages.objects.filter(company=profile.company)
        return context


class UnderCoverage(DetailView):
    model = UnderPackages
    template_name = 'accounts/under-coverage.html'
    context_object_name = 'details'

