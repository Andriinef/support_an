from django.urls import path

from support import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
]
