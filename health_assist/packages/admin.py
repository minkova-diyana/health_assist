from django.contrib import admin

from health_assist.packages.models import CompanyPackages, UnderPackages, Packages, Documents


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    pass
@admin.register(UnderPackages)
class UnderPackagesAdmin(admin.ModelAdmin):
    pass
@admin.register(CompanyPackages)
class CompanyPackagesAdmin(admin.ModelAdmin):
    pass