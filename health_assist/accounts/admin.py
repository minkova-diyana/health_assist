from django.contrib import admin

from health_assist.accounts.models import HnfUserModel, EmployeeProfile, InsuredCompanies


@admin.register(HnfUserModel)
class HnfUserModelAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)


@admin.register(InsuredCompanies)
class InsuredCompaniesAdmin(admin.ModelAdmin):
    pass
