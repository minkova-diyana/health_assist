from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from parler.utils.context import switch_language

from health_assist.web_pages.choices import TypeInsurance
from parler.models import TranslatableModel, TranslatedFields


class Pages(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    #  ATENTION EXPERIMENT ALSO IN THE TEMPLATS DON'T COMMIT!!!!


class InsuranceTypes(TranslatableModel):
    translations = TranslatedFields(
        type_insurance=models.CharField(
            max_length=100,
            null=True,
            blank=True
        ),
        description=models.TextField(null=False, blank=False)
    )

    def __str__(self):
        name_translation = self.get_translation('en')
        return f'{name_translation.type_insurance}'


class Information(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100, verbose_name=_("Title")),
        content=models.TextField(max_length=500, verbose_name=_("Content")),
        hidden_info=models.TextField(
            blank=True,
            null=True,
            verbose_name=_("Hidden information"),
        )
    )

    created_at = models.DateTimeField(auto_now_add=True)
    pages = models.ForeignKey(
        Pages,
        on_delete=models.CASCADE
    )

    type_insurance = models.ForeignKey(
        InsuranceTypes,
        on_delete=models.CASCADE,
        related_name='insurance_type',
        null=True,
        blank=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            title_translation = self.get_translation('en')
            self.slug = slugify(title_translation.title)

        super().save(*args, **kwargs)

    def __str__(self):
        name_translation = self.get_translation('en')
        return f'{name_translation.title}'


class Partners(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners')
    partner_url = models.URLField()

    def __str__(self):
        return self.name
