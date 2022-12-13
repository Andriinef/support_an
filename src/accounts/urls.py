from django.urls import path

from accounts import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "registration_home/",
        views.RegistrationHomePageView.as_view(),
        name="registration_home",
    ),
]
