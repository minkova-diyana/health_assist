from django.contrib import admin
from parler.admin import TranslatableAdmin

from health_assist.web_pages.models import Pages, Information


# Register your models here.
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Information)
class InformationAdmin(TranslatableAdmin):
    readonly_fields = ('slug',)
