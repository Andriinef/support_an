from dataclasses import dataclass, asdict
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.http import HttpResponse
import json


@dataclass
class Person:
    name: str
    age: int


def get_base(self):
    user_1 = Person(name="Andrii", age=45)
    content = json.dumps(asdict(user_1))
    content_type = "application/json"
    return HttpResponse(content, content_type=content_type)


urlpatterns = [
    path("base/", get_base),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    re_path(r"^images/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("", include("support.urls")),  # support
]
