from django.urls import path

from beta.views import Confirmation, Signup

urlpatterns = [
    path("signup/", Signup.as_view(), name="beta_signup"),
    path("signup/confirmed/", Confirmation.as_view(), name="beta_confirmation"),
]
