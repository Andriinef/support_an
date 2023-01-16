from rest_framework.generics import ListAPIView, RetrieveAPIView

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsListAPIView(ListAPIView):
    """Відображення спіска comment"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsRetrieveAPIView(RetrieveAPIView):
    """Відображення одного comment вказанного по id(pk)"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
