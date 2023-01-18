from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("accounts.urls"), name="accounts"),
    path("exchange-rates/", include("exchange_rates.urls"), name="exchange-rates"),
    path("api-auth/", include("rest_framework.urls")),  # auth
    path("dj-rest-auth/", include("dj_rest_auth.urls")),  # auth
    # path("dj-rest-auth/registration/",               # auth
    #      include("dj_rest_auth.registration.urls")),
    path("", include("core.urls"), name="core"),
    re_path(r"^images/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
