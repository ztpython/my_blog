from django.db import models
from apps.content.models import Post

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='名字')
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')

    class Meta:
        db_table = 'mb_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return "{}: {}".format(self.name, self.text[:20])