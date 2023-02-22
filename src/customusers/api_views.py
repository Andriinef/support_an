from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from customusers.models import User
from customusers.serializers import UserRegistrationSerializer, UserSerializer
from shared.serializers import ResponseMultiSerializer, ResponseSerializer


class UserCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    """ Дозволяє будь-якому користувачеві виконувати будь-яку дію """
    permission_classes = (AllowAny,)


class UserViewSet(ViewSet):
    def list(self, request) -> JsonResponse:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, pk: int) -> JsonResponse:
        user = User.objects.get(pk=pk)
        serializer = UserRegistrationSerializer(user)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request) -> JsonResponse:
        context = {"request": self.request}
        serializer = UserRegistrationSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()

            response = ResponseSerializer({"result": serializer.data})

            return JsonResponse(response.data, status=status.HTTP_201_CREATED)

        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk: int) -> JsonResponse:
        user = User.objects.get(pk=pk)
        context: dict = {
            "request": self.request,
        }
        serializer = UserRegistrationSerializer(user, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def destroy(self, request, pk: int) -> JsonResponse:
        user = User.objects.filter(pk=pk)
        user.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
