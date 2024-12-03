from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from health_assist.accounts.models import EmployeeProfile

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance: UserModel, created: bool, **kwargs):
    if created and not instance.is_staff:
        profile = EmployeeProfile.objects.get(uc_id_num=instance.uc_id_number)
        profile.user = instance
        profile.save()
