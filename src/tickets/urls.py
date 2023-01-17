from django.urls import path

from tickets.views import (TicketCreateAPIView, TicketListCreateAPIView,
                           TicketRetrieveAPIView, TicketRetrieveDestroyAPIView,
                           TicketRetrieveUpdateAPIView, TicketsListAPIView)

urlpatterns = [
    path("", TicketsListAPIView.as_view()),
    # path("create/", create_ticket),
    path("create/", TicketCreateAPIView.as_view()),
    path("listcreate/", TicketListCreateAPIView.as_view()),
    path("retrieveupdate/<slug:slug>/", TicketRetrieveUpdateAPIView.as_view()),
    path("retrievedestroy/<slug:slug>/", TicketRetrieveDestroyAPIView.as_view()),
    path("<slug:slug>/", TicketRetrieveAPIView.as_view()),
]
