from django.urls import path

from tickets.views import TicketRetrieveAPIView, TicketsGet

urlpatterns = [
    path("", TicketsGet.as_view(), name="tickets_ticket"),
    path("<int:pk>/", TicketRetrieveAPIView.as_view()),
]
