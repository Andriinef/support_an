from django.urls import path

from customusers.api_views import (UserCreateAPIView, customuser_detail,
                                   customusers_list_create)

urlpatterns = [
    path("", customusers_list_create),
    path("<int:id_>/", customuser_detail),
    path("create/", UserCreateAPIView.as_view()),
]
