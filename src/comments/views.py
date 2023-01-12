from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsGet(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailGet(ListAPIView):
    def get(self, request, pk):
        queryset = Comment.objects.get(id=pk)
        serializer = CommentSerializer(queryset)
        return Response(serializer.data)
