from django.apps import AppConfig

class SricrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sricrm'

    def ready(self):
        from knox import auth
        import secrets

        def custom_generate_token_string():
            return secrets.token_hex(64)

        auth.generate_token_string = custom_generate_token_string
