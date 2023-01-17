from rest_framework.serializers import ModelSerializer, SlugRelatedField

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", read_only=True)
    ticket = SlugRelatedField(slug_field="header", read_only=True)

    class Meta:
        fields = "__all__"
        # exclude = ("id",)
        model = Comment
