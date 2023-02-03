from django.contrib import admin
from django.urls import include, path

from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls"), name="exchange-rates"),
    path("api-auth/", include("rest_framework.urls")),  # auth
    path("", include("core.urls"), name="core"),
    # path("accounts/", include("accounts.urls"), name="accounts"),
    # path("dj-rest-auth/", include("dj_rest_auth.urls")),  # auth
    # path("dj-rest-auth/registration/",               # auth
    #      include("dj_rest_auth.registration.urls")),
    # path("djoser-auth/", include("djoser.urls")),
] + yasg_urls
