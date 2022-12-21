from django.urls import include, path

from accounts import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "accounts_home/",
        views.RegistrationHomePageView.as_view(),
        name="registration_home",
    ),
]
