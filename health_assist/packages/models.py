from django.db import models
from django.template.defaultfilters import slugify

from health_assist.accounts.models import InsuredCompanies, HnfUserModel
from health_assist.packages.path_creation import user_directory_path
from health_assist.packages.validators import FileSizeValidator


# Create your models here.
class Documents(models.Model):
    type_document = models.CharField(max_length=100)

    def __str__(self):
        return self.type_document


class Packages(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UnderPackages(models.Model):
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='under_packages')
    company = models.ForeignKey(InsuredCompanies, on_delete=models.CASCADE, related_name='under_company')
    name = models.CharField(max_length=100)
    limit = models.CharField(max_length=255, blank=False, null=False)
    coverage = models.TextField(blank=False, null=False)
    documents_needed = models.ManyToManyField(Documents, related_name='documents')
    slug = models.SlugField(
        max_length=100,
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class CompanyPackages(models.Model):
    company = models.ForeignKey(InsuredCompanies, on_delete=models.CASCADE, related_name='company_packages')
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='company_under_packages')

    def __str__(self):
        return f'{self.company.name} - {self.packages.name}'


class ReimbursementClaims(models.Model):
    document = models.ForeignKey(Documents, on_delete=models.CASCADE, related_name='uploaded_documents', default=0)
    under_package = models.ForeignKey(UnderPackages, on_delete=models.CASCADE, related_name='uploaded_documents', default=0)
    user = models.ForeignKey(HnfUserModel, on_delete=models.CASCADE, related_name='uploaded_documents', default=0)
    file = models.FileField(upload_to=user_directory_path, validators=[FileSizeValidator(max_size_mb=1)])
    uploaded_at = models.DateTimeField(auto_now_add=True)
