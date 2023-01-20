from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

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

    """ Дозволяє аутентифікованим користувачам виконувати будь-яку дію,
     а неаутентифікованим – лише GET """
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketCreateAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketRetrieveAPIView(RetrieveAPIView):
    """Забезпечуює доступ до інформації про окремий
    об'єкт"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"
    """ Дозволяє аутентифікованим користувачам виконувати будь-яку дію """
    permission_classes = (IsAuthenticated,)


class TicketListCreateAPIView(ListCreateAPIView):
    """Читання та створення спіска ticket"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Забезпечуює доступ до інформації про окремий
    об'єкт та дозволяє його оновлювати"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TicketRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """Забезпечуює доступ до інформації про окремий
    об'єкт та дозволяє його видилити"""

    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    lookup_field = "slug"

    """ Дозволяє лише адміністраторам виконувати будь-яку дію """
    permission_classes = (IsAdminUser,)
