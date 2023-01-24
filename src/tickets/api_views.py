from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ViewSet

from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import (TicketLightSerializer, TicketModelSerializer,
                                 TicketSerializer)


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


class TicketAPISet(ViewSet):
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)


tickets_list = TicketAPISet.as_view({"get": "list"})
ticket_create = TicketAPISet.as_view({"post": "create"})
ticket_retrieve = TicketAPISet.as_view({"get": "retrieve"})
