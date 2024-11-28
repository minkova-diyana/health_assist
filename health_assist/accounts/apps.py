from django.apps import AppConfig


class AccontsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_assist.accounts'

    def ready(self):
        import health_assist.accounts.signals