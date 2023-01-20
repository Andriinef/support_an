from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from customusers.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    """ Дозволяє будь-якому користувачеві виконувати будь-яку дію """
    permission_classes = (AllowAny,)
