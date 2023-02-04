from typing import Any

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from customusers.constants import Role
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser
from tickets.serializers import (
    TicketLightSerializer,
    TicketModelSerializer,
    TicketSerializer,
)


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()
    model = Ticket
    serializer_class = TicketSerializer
    # permission_classes = [
    #     RoleIsManager | RoleIsAdmin
    #     if ModelViewSet.action == "list"
    #     else RoleIsUser
    #     if ModelViewSet.action == "create"
    #     else IsOwner | RoleIsAdmin | RoleIsManager
    #     if ModelViewSet.action == "retrieve"
    #     else RoleIsManager | RoleIsAdmin
    #     if ModelViewSet.action == "update"
    #     else RoleIsManager | RoleIsAdmin
    #     if ModelViewSet.action == "destroy"N
    #     else []
    # ]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = (RoleIsManager | RoleIsAdmin,)
        elif self.action == "create":
            permission_classes = (RoleIsUser | IsOwner | RoleIsAdmin,)
        elif self.action == "retrieve":
            permission_classes = (RoleIsUser | IsOwner | RoleIsManager | RoleIsAdmin,)
        elif self.action == "update":
            permission_classes = (RoleIsManager | RoleIsAdmin,)
        elif self.action == "destroy":
            permission_classes = (RoleIsManager | RoleIsAdmin,)
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs) -> Response:
        if request.user.role == Role.ADMIN:
            queryset = self.get_queryset()
        else:
            queryset = Ticket.objects.filter(manager=request.user)

        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        serializer = TicketModelSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return Response(response.data)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        context = {"request": request}
        serializer = TicketModelSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return Response(response.data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()

        context = {"request": request}
        serializer = TicketModelSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return Response(response.data, status=status.HTTP_201_CREATED)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        pk = kwargs.get("pk")
        instance = Ticket.objects.filter(pk=pk)
        instance.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


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
