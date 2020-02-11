# 在这里存放表单代码
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        # 指定表单对应的数据库模型是Comment类
        model = Comment
        # 指定表单要显示的字段
        fields = ['name', 'email', 'url', 'text']