from rest_framework.generics import ListAPIView, RetrieveAPIView

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsGet(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
