from django.apps import AppConfig


class PhotostoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photostore'


    def ready(self):
        import photostore.signals
