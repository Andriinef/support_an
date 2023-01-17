from rest_framework.serializers import (CurrentUserDefault, HiddenField,
                                        ModelSerializer, SlugRelatedField)

from tickets.models import Ticket


class TicketSerializer(ModelSerializer):
    customer = SlugRelatedField(slug_field="email", read_only=True)
    manager = SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        fields = "__all__"
        # exclude = ("id",)
        model = Ticket


class TicketModelSerializer(ModelSerializer):
    customer = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ["customer", "manager", "header", "body", "slug"]
        model = Ticket
