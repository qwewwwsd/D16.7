from django.apps import AppConfig


class App3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_3'

    def ready(self):
        from .import signals

