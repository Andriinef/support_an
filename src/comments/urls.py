from django.urls import path

from comments.views import CommentsGet, CommentsRetrieveAPIView

urlpatterns = [
    path("", CommentsGet.as_view()),
    path("<int:pk>/", CommentsRetrieveAPIView.as_view()),
]
