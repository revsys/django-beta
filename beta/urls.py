from django.conf.urls import url

from beta.views import Signup, Confirmation


urlpatterns = [
    url(r"^signup/$", view=Signup.as_view(), name="beta_signup"),
    url(r"^signup/confirmed/$", view=Confirmation.as_view(), name="beta_confirmation"),
]
