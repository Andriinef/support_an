from django.urls import include, path

urlpatterns = [
    path("tickets/", include("tickets.urls"), name="tickets"),
    path("comments/", include("comments.urls"), name="comments"),
    path("customusers/", include("customusers.urls"), name="customusers"),
]
