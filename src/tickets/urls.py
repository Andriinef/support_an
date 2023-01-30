from django.urls import path
from rest_framework.routers import DefaultRouter

from tickets.api_views import (TicketAPISet, TicketCreateAPIView,
                               TicketListCreateAPIView, TicketRetrieveAPIView,
                               TicketRetrieveDestroyAPIView,
                               TicketRetrieveUpdateAPIView, TicketsListAPIView)

router = DefaultRouter()
router.register(r"tickets", TicketAPISet, basename="tickets")


urlpatterns = [
    path("list/", TicketsListAPIView.as_view()),
    path("create/", TicketCreateAPIView.as_view()),
    path("listcreate/", TicketListCreateAPIView.as_view()),
    path("retrieve/<slug:slug>/", TicketRetrieveAPIView.as_view()),
    path("retrieveupdate/<slug:slug>/", TicketRetrieveUpdateAPIView.as_view()),
    path("retrievedestroy/<slug:slug>/", TicketRetrieveDestroyAPIView.as_view()),
] + router.urls
