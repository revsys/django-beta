from django.conf.urls.defaults import *

from beta.views import Signup, Confirmation

urlpatterns = patterns('',
    url(
        regex = '^signup/$',
        view = Signup.as_view(),
        name = 'beta_signup',
        ),
    url(
        regex = '^signup/confirmed/$',
        view = Confirmation.as_view(),
        name = 'beta_confirmation',
        ),
    )
