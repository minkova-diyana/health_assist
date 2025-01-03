from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from health_assist.web_pages.choices import TypeInsurance


class Pages(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Information(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    content = models.TextField(max_length=500)
    hidden_info = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    pages = models.ForeignKey(
        Pages,
        on_delete=models.CASCADE
    )
    type_insurance = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=TypeInsurance.choices
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Partners(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners')
    partner_url = models.URLField()
