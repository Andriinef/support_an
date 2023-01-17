from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view

from tickets.models import Ticket
from tickets.serializers import TicketCreateSerializer, TicketModelSerializer


@api_view(["POST"])
def create_ticket(request) -> JsonResponse:
    serializer = TicketCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Ticket.objects.create(**serializer.validated_data)
    return JsonResponse(serializer.validated_data)


class TicketsListAPIView(generics.ListAPIView):
    """Відображення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer


class TicketRetrieveAPIView(generics.RetrieveAPIView):
    """Відображення одного ticket вказанного по id(pk)"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"


class TicketListCreateAPIView(generics.ListCreateAPIView):
    """Читання та створення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
