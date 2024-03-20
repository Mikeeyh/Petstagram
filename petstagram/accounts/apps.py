from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram.accounts'

    def ready(self):  # Importing signals manually because it is not build-in, it will not create a profile of the user
        import petstagram.accounts.signals
