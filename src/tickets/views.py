from rest_framework import generics

from tickets.models import Ticket
from tickets.serializers import TicketModelSerializer


class TicketsListAPIView(generics.ListAPIView):
    """Відображення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer


class TicketRetrieveAPIView(generics.RetrieveAPIView):
    """Відображення одного ticket вказанного по id(pk)"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "id"


class TicketListCreateAPIView(generics.ListCreateAPIView):
    """Читання та створення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
