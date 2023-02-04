from rest_framework import serializers

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        # exclude = ("id",)
        model = Ticket


class TicketModelSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # manager = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Ticket
        fields = ["id", "header", "body", "customer", "slug"]


class TicketLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ["body", "manager"]
