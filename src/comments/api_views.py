from rest_framework.generics import CreateAPIView, ListAPIView

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentsCreateAPI(CreateAPIView):
    serializer_class = CommentSerializer
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def get_queryset(self):
        ticket_id: int = self.kwargs[self.lookup_field]
        return Comment.objects.filter(ticket_id=ticket_id)


class CommentsListAPI(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
