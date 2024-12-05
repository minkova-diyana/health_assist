from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from health_assist.accounts.managers import AccountsUserManager
from health_assist.encriptsion import encrypt_data


# Create your models here.

class InsuredCompanies(models.Model):
    name = models.CharField(max_length=100)
    insurance_company_name = models.CharField(max_length=100, null=True, blank=True)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()

    def __str__(self):
        return self.name


class HnfUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AccountsUserManager()

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    uc_id_number = models.TextField(unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    USERNAME_REQUIRED_FIELDS = ['uc_id_number']

    def save(self, *args, **kwargs):
        if not self.uc_id_number and not self.is_staff:
            raise ValueError('Must have UCN')
        super().save(*args, **kwargs)


class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        HnfUserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='employee_profile',
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    uc_id_num = models.TextField(unique=True)
    company = models.ForeignKey(
        InsuredCompanies,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        self.uc_id_num = encrypt_data(self.uc_id_num)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.company.name}'
