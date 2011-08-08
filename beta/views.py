from django.views import generic

from beta.models import BetaSignup 
from beta.forms import BetaSignupForm

class Signup(generic.CreateView):
    """ View to handle beta signup """
    template_name = 'beta/signup.html' 
    form_class = BetaSignupForm

