from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core'

    def ready(self):
        # Override default admin site with custom dashboard
        from config.admin import GirasolAdminSite  # noqa: F401
