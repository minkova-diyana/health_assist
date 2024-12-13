from django.apps import AppConfig


class WebPagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_assist.web_pages'

    def ready(self):
        import health_assist.web_pages.signals