import cloudinary.uploader
from django.db import models
from django.template.defaultfilters import slugify

from health_assist.accounts.models import InsuredCompanies, HnfUserModel
from health_assist.packages.path_creation import user_directory_path
from parler.models import TranslatableModel, TranslatedFields
from cloudinary.models import CloudinaryField


# Create your models here.
class Documents(TranslatableModel):
    translations = TranslatedFields(
        type_document=models.CharField(max_length=100)
    )

    # def __str__(self):
    #     name_translation = self.get_translation('en')
    #     return f'{name_translation.name}'


class Packages(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )

    def __str__(self):
        name_translation = self.get_translation('en')
        return f'{name_translation.name}'


class UnderPackages(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        limit=models.CharField(max_length=255, blank=False, null=False),
        coverage=models.TextField(blank=False, null=False),
    )
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='under_packages')
    company = models.ForeignKey(InsuredCompanies, on_delete=models.CASCADE, related_name='under_company')

    documents_needed = models.ManyToManyField(Documents, related_name='documents')
    slug = models.SlugField(
        max_length=100,
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            name_translation = self.get_translation('en')
            self.slug = slugify(name_translation.name)
        super().save(*args, **kwargs)

    def __str__(self):
        name_translation = self.get_translation('en')
        return f'{name_translation.name}'


class CompanyPackages(models.Model):
    company = models.ForeignKey(InsuredCompanies, on_delete=models.CASCADE, related_name='company_packages')
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='company_under_packages')

    def __str__(self):
        return f'{self.company.name} - '


class ReimbursementClaims(models.Model):
    document = models.ForeignKey(
        Documents,
        on_delete=models.CASCADE,
        related_name='reimbursement_claims_documents',
    )
    under_package = models.ForeignKey(
        UnderPackages,
        on_delete=models.CASCADE,
        related_name='reimbursement_claims_packages',
    )
    user = models.ForeignKey(
        HnfUserModel,
        on_delete=models.CASCADE,
        related_name='reimbursement_claims_users',
    )
    file = CloudinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file:
            file_path = user_directory_path(self, self.file.name)

            upload_response = cloudinary.uploader.upload(
                self.file,
                folder=file_path.rsplit('/', 1)[0],
                public_id=file_path.split('/')[-1].split('.')[0],

            )

            self.file = upload_response.get('public_id')

        super().save(*args, **kwargs)
