from django.urls import path

from comments.api_views import CommentsListAPIView, CommentsRetrieveAPIView

urlpatterns = [
    path("", CommentsListAPIView.as_view()),
    path("<int:pk>/", CommentsRetrieveAPIView.as_view()),
]
