from django.contrib import admin
from parler.admin import TranslatableAdmin

from health_assist.packages.models import CompanyPackages, UnderPackages, Packages, Documents, UnderPackageNames


@admin.register(Documents)
class DocumentsAdmin(TranslatableAdmin):
    pass


@admin.register(Packages)
class PackagesAdmin(TranslatableAdmin):
    pass


@admin.register(UnderPackages)
class UnderPackagesAdmin(TranslatableAdmin):
    pass


@admin.register(CompanyPackages)
class CompanyPackagesAdmin(admin.ModelAdmin):
    pass


@admin.register(UnderPackageNames)
class UnderPackageNamesAdmin(TranslatableAdmin):
    pass
