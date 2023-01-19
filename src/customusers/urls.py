from django.urls import path

from customusers.api_views import UserCreateAPIView

urlpatterns = [path("", UserCreateAPIView.as_view())]
