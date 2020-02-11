from django.db import models
from ..user.models import User

import markdown
from django.utils.html import strip_tags

# Create your models here.

class Tag(models.Model):
    # 标签
    name = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mb_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Category(models.Model):
    # 分类
    name = models.CharField(max_length=100, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mb_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Post(models.Model):
    # 文章
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField(verbose_name='正文')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    excerpt = models.CharField(max_length=200, blank=True, verbose_name='文章摘要')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        # 在后台显示字段名
        return self.title

    def save(self, *args, **kwargs):
        # 重写save方法,实现部分功能

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 10 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:10]

        super().save(*args, **kwargs)


    class Meta:
        db_table = 'mb_post'
        verbose_name = '正文'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']