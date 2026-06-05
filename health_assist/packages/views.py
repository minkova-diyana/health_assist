from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from health_assist.accounts.models import EmployeeProfile
from health_assist.packages.forms import UploadFiles
from health_assist.packages.models import (
    CompanyPackages,
    UnderPackages,
    ReimbursementClaims,
    Documents
)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        package = self.object

        required_docs = package.documents_needed.all()

        user_claims = ReimbursementClaims.objects.filter(
            user=self.request.user,
            under_package=package
        )

        uploaded_map = {
            claim.document_id: claim
            for claim in user_claims
        }

        uploaded_ids = set(uploaded_map.keys())

        context.update({
            "required_docs": required_docs,
            "uploaded_ids": uploaded_ids,
            "uploaded_map": uploaded_map,
            "uploaded_count": len(uploaded_ids),
            "required_count": required_docs.count(),
            "progress": (
                len(uploaded_ids) / required_docs.count() * 100
                if required_docs.exists() else 0
            ),
        })

        return context


class UploadFilesView(LoginRequiredMixin, CreateView):
    model = ReimbursementClaims
    form_class = UploadFiles
    template_name = 'packages/upload-document.html'

    def dispatch(self, request, *args, **kwargs):
        self.under_package = get_object_or_404(
            UnderPackages,
            slug=self.kwargs['under_package_slug']
        )
        self.document = get_object_or_404(
            Documents,
            pk=self.kwargs['document_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        required_docs = self.under_package.documents_needed.all()

        uploaded_docs = ReimbursementClaims.objects.filter(
            user=self.request.user,
            under_package=self.under_package
        ).values_list('document_id', flat=True)

        uploaded_docs_set = set(uploaded_docs)

        context.update({
            "under_package": self.under_package,
            "document": self.document,
            "required_documents": required_docs,
            "uploaded_docs": uploaded_docs_set,
            "uploaded_count": len(uploaded_docs_set),
            "required_count": required_docs.count(),
            "progress": (
                len(uploaded_docs_set) / required_docs.count() * 100
                if required_docs.exists() else 0
            ),
        })

        return context

    def form_valid(self, form):
        uploaded_file = form.save(commit=False)

        uploaded_file.document = self.document
        uploaded_file.under_package = self.under_package
        uploaded_file.user = self.request.user

        uploaded_file.save()

        return redirect(
            'under-package',
            self.under_package.pk  # safer than pk if your URL uses slug
        )


class UploadClaimFileView(LoginRequiredMixin, CreateView):
    model = ReimbursementClaims
    form_class = UploadFiles

    def form_valid(self, form):
        package = get_object_or_404(
            UnderPackages,
            slug=self.kwargs['under_package_slug']
        )

        document = get_object_or_404(
            Documents,
            pk=self.kwargs['document_id']
        )

        claim, created = ReimbursementClaims.objects.get_or_create(
            user=self.request.user,
            document=document,
            under_package=package
        )

        claim.file = form.cleaned_data['file']
        claim.save()

        return JsonResponse({
            "success": True,
            "document_name": document.type_document,
            "document_id": document.id
        })