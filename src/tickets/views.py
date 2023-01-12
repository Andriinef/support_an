from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.serializers import TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailGet(ListAPIView):
    def get(self, request, pk):
        queryset = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(queryset)
        return Response(serializer.data)
