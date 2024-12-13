from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from health_assist.accounts.models import EmployeeProfile
from health_assist.packages.forms import UploadFiles
from health_assist.packages.models import CompanyPackages, UnderPackages, ReimbursementClaims, Documents


class UserPackage(ListView):
    model = UnderPackages
    template_name = 'packages/account-insurance-package.html'
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
    template_name = 'packages/under-coverage.html'
    context_object_name = 'details'


class UploadFilesView(LoginRequiredMixin, CreateView):
    model = ReimbursementClaims
    form_class = UploadFiles
    template_name = 'packages/upload-document.html'

    def get_context_data(self, **kwargs):
        under_package_slug = self.kwargs['under_package_slug']
        document_id = self.kwargs['document_id']
        document = get_object_or_404(Documents, pk=document_id)
        under_package = get_object_or_404(UnderPackages, slug=under_package_slug)
        required_documents = under_package.documents_needed.all()

        context = super().get_context_data(**kwargs)
        context['required_documents'] = required_documents
        context['under_package'] = under_package
        context['document'] = document
        return context

    def form_valid(self, form):
        under_package_slug = self.kwargs['under_package_slug']
        document_id = self.kwargs['document_id']
        document = get_object_or_404(Documents, pk=document_id)
        under_package = get_object_or_404(UnderPackages, slug=under_package_slug)

        uploaded_file = form.save(commit=False)
        uploaded_file.document = document
        uploaded_file.under_package = under_package
        uploaded_file.user = self.request.user
        uploaded_file.save()

        return redirect('under-package', under_package.pk)

    def get_success_url(self):
        under_package_slug = self.kwargs['under_package_slug']
        under_package = get_object_or_404(UnderPackages, slug=under_package_slug)

        return reverse_lazy('under-package', under_package.pk)
