from django.urls import path

from tickets import views

urlpatterns = [
    path("", views.TicketsListAPIView.as_view()),
    path("<int:id>/", views.TicketRetrieveAPIView.as_view()),
    path("apiview/", views.TicketListCreateAPIView.as_view()),
]
