from django.apps import AppConfig


class BetaConfig(AppConfig):
    name = "beta"

    def ready(self):
        from beta import listeners
