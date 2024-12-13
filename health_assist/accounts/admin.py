
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from health_assist.accounts.models import HnfUserModel, EmployeeProfile, InsuredCompanies


@admin.register(HnfUserModel)
class HnfUserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'uc_id_number')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
#
#
# class HnfUserAdmin(BaseUserAdmin):
#     add_form = EmployeeRegistrationForm
#     form = EmployeeRegistrationForm
#     model = HnfUserModel
#     list_display = ('email', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'uc_id_number')}),
#         (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#          ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#
#
# admin.site.register(HnfUserModel, HnfUserAdmin)


# Register your models here.
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)


@admin.register(InsuredCompanies)
class InsuredCompaniesAdmin(admin.ModelAdmin):
    pass
