from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="email", read_only=True)
    ticket = serializers.SlugRelatedField(slug_field="header", read_only=True)

    class Meta:
        fields = "__all__"
        # exclude = ("id",)
        model = Comment
