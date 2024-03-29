from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from customusers.constants import Role

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

    #     _read_only_fields = ["email"]  # поля лише для читання
    #     _write_only_fields = ["password"]  # поля лише для запису

    # def create(self, validated_data):
    #     user = User.objects.create(  # створення та валидация данних
    #         email=validated_data["email"],
    #     )

    #     user.set_password(
    #         validated_data["password"]
    #     )  # алгоритм хешування пароля (за замовчуванням це bcrypt)
    #     user.save()

    #     return user

    """ другий варіант хешування пароля """

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        attrs["role"] = Role.USER
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
