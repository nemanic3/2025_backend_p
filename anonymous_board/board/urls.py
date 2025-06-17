from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView, CommentView

urlpatterns = [
    path('posts', PostListCreateAPIView.as_view()),
    path('posts/<int:post_id>', PostDetailAPIView.as_view()),
    path('posts/<int:post_id>/comment', CommentView.as_view()),
]
