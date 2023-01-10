from django.urls import path

from tickets.views import TicketsGet

urlpatterns = [
    path("", TicketsGet.as_view(), name="tickets_ticket"),
]
