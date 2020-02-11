from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # 创建用户模型,继承自Django自带的用户认证
    pass

    class Meta:
        db_table = 'mb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

