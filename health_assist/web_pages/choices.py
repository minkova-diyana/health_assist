from django.db import models


class TypeInsurance(models.TextChoices):
    GENERAL = 'general', 'general'
    HEALTH = 'health', 'health'
