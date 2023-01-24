from django.urls import path

from customusers.api_views import (UserCreateAPIView, customuser_create,
                                   customuser_retrieve, customusers_list)

urlpatterns = [
    path("", customusers_list),
    path("", customuser_create),
    path("<int:id_>/", customuser_retrieve),
    path("create/", UserCreateAPIView.as_view()),
]
