from django.urls import include, path

urlpatterns = [
    path("beta/", include("beta.urls")),
]
