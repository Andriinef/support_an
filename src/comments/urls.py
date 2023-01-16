from django.urls import path

from comments.views import CommentsListAPIView, CommentsRetrieveAPIView

urlpatterns = [
    path("", CommentsListAPIView.as_view()),
    path("<int:pk>/", CommentsRetrieveAPIView.as_view()),
]
