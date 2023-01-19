from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from tickets.models import Ticket
from tickets.serializers import TicketModelSerializer, TicketSerializer


@api_view(["POST"])
def create_ticket(request) -> JsonResponse:
    serializer = TicketModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Ticket.objects.create(**serializer.validated_data)
    return JsonResponse(serializer.validated_data)


class TicketsListAPIView(ListAPIView):
    """Відображення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketCreateAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer


class TicketRetrieveAPIView(RetrieveAPIView):
    """Відображення одного ticket вказанного по id(pk)"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketListCreateAPIView(ListCreateAPIView):
    """Читання та створення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer


class TicketRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"
    permission_classes = (IsAdminUser,)
