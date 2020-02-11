from django.urls import path
from .views import CommentView

app_name = 'comments'
urlpatterns = [
    path('<int:post_id>', CommentView.as_view(), name='comments'),  # 评论
]
