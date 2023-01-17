from django.urls import path

from tickets import views

urlpatterns = [
    path("", views.TicketsListAPIView.as_view()),
    path("create/", views.create_ticket),
    path("listcreate/", views.TicketListCreateAPIView.as_view()),
    path("<slug:slug>/", views.TicketRetrieveAPIView.as_view()),
]
