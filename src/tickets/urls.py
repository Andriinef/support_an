from django.urls import path

from .views import (TicketListCreateAPIView, TicketRetrieveAPIView,
                    TicketsListAPIView)

urlpatterns = [
    path("", TicketsListAPIView.as_view()),
    path("<int:id>/", TicketRetrieveAPIView.as_view()),
    path("apiview/", TicketListCreateAPIView.as_view()),
]
