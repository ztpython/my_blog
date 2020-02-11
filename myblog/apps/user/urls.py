from django.urls import path, include
from .views import Login

app_name = 'user'
urlpatterns = [
    path('', Login.as_view(), name='login'),  # 用户模块配置
]
