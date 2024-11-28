from django.contrib import admin

from health_assist.web_pages.models import Pages, Information


# Register your models here.
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
