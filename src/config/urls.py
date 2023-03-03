from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from .openapi import urlpatterns as openapi_urls

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("api-auth/", include("rest_framework.urls")),  # auth
    path("", include("core.urls"), name="core"),
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
    # path("accounts/", include("accounts.urls"), name="accounts"),
    # path("dj-rest-auth/", include("dj_rest_auth.urls")),  # auth
    # path("dj-rest-auth/registration/",               # auth
    #      include("dj_rest_auth.registration.urls")),
    # path("djoser-auth/", include("djoser.urls")),
] + openapi_urls

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()
