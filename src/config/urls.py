from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from .yasg import urlpatterns as yasg_urls

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls"), name="exchange-rates"),
    path("api-auth/", include("rest_framework.urls")),  # auth
    path("", include("core.urls"), name="core"),
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
    # path("accounts/", include("accounts.urls"), name="accounts"),
    # path("dj-rest-auth/", include("dj_rest_auth.urls")),  # auth
    # path("dj-rest-auth/registration/",               # auth
    #      include("dj_rest_auth.registration.urls")),
    # path("djoser-auth/", include("djoser.urls")),
] + yasg_urls

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()
