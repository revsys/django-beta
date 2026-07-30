from django.apps import AppConfig


class BetaConfig(AppConfig):
    name = "beta"
    verbose_name = "Beta"
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        # Importing the module connects the post_save signal handler.
        from beta import listeners  # noqa: F401
