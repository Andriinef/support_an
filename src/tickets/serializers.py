from rest_framework import serializers

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field="email", read_only=True)
    manager = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        fields = "__all__"
        # exclude = ("id",)
        model = Ticket
