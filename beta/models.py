from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from beta.managers import BetaManager


class BetaSignup(models.Model):
    """
    Model to store our pre-beta signups
    """

    first_name = models.CharField(_("First Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=75, blank=True)
    email = models.EmailField(_("Email Address"), unique=True)

    contacted = models.BooleanField(_("Contacted"), default=False)
    registered = models.BooleanField(_("Registered"), default=False)

    created = models.DateTimeField(_("Created"), default=timezone.now)

    objects = BetaManager()

    class Meta:
        verbose_name = _("Beta Signup")
        verbose_name_plural = _("Beta Signups")

    def __str__(self):
        return f"Beta Signup - {self.email}"
