from django.urls import include, path

urlpatterns = [
    path("", include("tickets.urls"), name="tickets"),
    path("comments/", include("comments.urls"), name="comments"),
    path("customusers/", include("customusers.urls"), name="customusers"),
    path("authentication/", include("authentication.urls"), name="authentication"),
]
