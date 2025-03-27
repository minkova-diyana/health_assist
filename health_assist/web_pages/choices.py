from django.db import models


class TypeInsurance(models.TextChoices):
    ESTATE = 'estate', 'estate'
    AUTO = 'auto', 'auto'
    BUSINESS = 'business', 'business'
    HEALTH = 'health', 'health'
