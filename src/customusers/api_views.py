from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from customusers.models import User
from customusers.serializers import UserRegistrationSerializer, UserSerializer
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser


class UserCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    """ Дозволяє будь-якому користувачеві виконувати будь-яку дію """
    permission_classes = (AllowAny,)


class UserViewSet(ViewSet):
    def get_permissions(self):
        if self.action == "list":
            permission_classes = (RoleIsUser | RoleIsManager | RoleIsAdmin,)
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

    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, pk: int):
        user = User.objects.get(pk=pk)
        serializer = UserRegistrationSerializer(user)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request):
        context = {"request": self.request}
        serializer = UserRegistrationSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()

            response = ResponseSerializer({"result": serializer.data})

            return JsonResponse(response.data, status=status.HTTP_201_CREATED)

        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk: int):
        user = User.objects.get(pk=pk)
        context: dict = {
            "request": self.request,
        }
        serializer = UserRegistrationSerializer(user, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def destroy(self, request, pk: int):
        user = User.objects.filter(pk=pk).first()
        user.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
