from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from customusers.serializers import UserRegistrationSerializer, UserSerializer
from shared.serializers import ResponseMultiSerializer, ResponseSerializer

User = get_user_model()


class UserCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    """ Дозволяє будь-якому користувачеві виконувати будь-яку дію """
    permission_classes = (AllowAny,)


class UserViewSet(ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        user = User.objects.get(id=id_)
        serializer = UserSerializer(user)
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = ResponseSerializer({"result": serializer.data})
            return JsonResponse(response.data, status=status.HTTP_201_CREATED)
        return JsonResponse(response.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id_: int):
        user = User.objects.get(id=id_)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)


customusers_list = UserViewSet.as_view({"get": "list"})
customuser_create = UserViewSet.as_view({"post": "create"})
customuser_retrieve = UserViewSet.as_view({"get": "retrieve"})
customuser_update = UserViewSet.as_view({"post": "update"})
