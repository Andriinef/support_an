from django.urls import path

from tickets.views import TicketDetailGet, TicketsGet

urlpatterns = [
    path("", TicketsGet.as_view(), name="tickets_ticket"),
    path("<int:pk>/", TicketDetailGet.as_view()),
]
