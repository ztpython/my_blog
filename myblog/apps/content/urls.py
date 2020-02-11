from django.urls import path, include
from .views import IndexView, DetailView, ArchivesView, CategoryView, TagView

app_name = 'content'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:page>', IndexView.as_view(), name='index'),  # 博客正文第page页
    path('detail/<int:post_id>', DetailView.as_view(), name='detail'),  # 正文详情
    path('archive/<int:year>/<int:month>/<int:day>', ArchivesView.as_view(), name='archive'),  # 归档展示文章列表
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),  # 根据分类显示文章
    path('tag/<int:tag_id>', TagView.as_view(), name='tag'),  # 根据标签云显示文章

]
