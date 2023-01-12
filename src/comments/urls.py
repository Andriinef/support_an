from django.urls import path

from comments.views import CommentDetailGet, CommentsGet

urlpatterns = [
    path("", CommentsGet.as_view()),
    path("<int:pk>/", CommentDetailGet.as_view()),
]
