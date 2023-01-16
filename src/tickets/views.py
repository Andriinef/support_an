from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView

from tickets.models import Ticket
from tickets.serializers import TicketModelSerializer


class TicketsListAPIView(ListAPIView):
    """Відображення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer


class TicketRetrieveAPIView(RetrieveAPIView):
    """Відображення одного ticket вказанного по id(pk)"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "id"


class TicketListCreateAPIView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
