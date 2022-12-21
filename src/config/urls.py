import json
from dataclasses import asdict, dataclass

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("exchange-rates/", include("exchange_rates.urls"), name="exchange-rates"),
    re_path(r"^images/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
