from rest_framework.generics import ListAPIView, RetrieveAPIView

from tickets.models import Ticket
from tickets.serializers import TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketRetrieveAPIView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
