from django.urls import reverse
from django.views import generic

from beta.forms import BetaSignupForm


class Signup(generic.CreateView):
    """ View to handle beta signup """

    template_name = "beta/signup.html"
    form_class = BetaSignupForm

    def get_success_url(self):
        return reverse("beta_confirmation")


class Confirmation(generic.TemplateView):
    """ Confirmation Page """

    template_name = "beta/confirmation.html"
