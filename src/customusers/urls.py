# from django.urls import path
from rest_framework.routers import DefaultRouter

from customusers.api_views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    # path("", customusers_list_create),
    # path("<int:pk>/", customuser_detail),
    # path("create/", UserCreateAPIView.as_view()),
] + router.urls
