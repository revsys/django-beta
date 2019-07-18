from django.db.models.signals import post_save
from django.contrib.auth.models import User

from beta.models import BetaSignup


def user_post_save_callback(sender, instance, created, **kwargs):
    """ Mark a user as registered if a real User object is created """
    if created:
        matches = BetaSignup.objects.filter(email=instance.email)

        if matches:
            matches[0].registered = True
            matches[0].save()


post_save.connect(user_post_save_callback, sender=User)
