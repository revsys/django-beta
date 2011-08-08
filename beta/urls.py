from django.conf.urls.defaults import *

from beta.views import Signup

urlpatterns = patterns('',
    url(
        regex = '^signup/$',
        view = Signup.as_view(),
        name = 'beta_signup',
        ),
    )
