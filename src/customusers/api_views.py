from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from customusers.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    """ Дозволяє будь-якому користувачеві виконувати будь-яку дію """
    permission_classes = (AllowAny,)
