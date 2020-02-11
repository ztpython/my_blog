from django import template
from ..forms import CommentForm

# 自定义模板标签实现生成表单

# 1 先实例化一个template.Library(), 进行注册
register = template.Library()

# 2 定义一个 inclusion_tag 类型的模板标签，用于渲染评论表单
@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }

# 3 定义一个inclusion_tag类型的模板标签,实现显示所有评论及数量
@register.inclusion_tag('comments/inclusions/_comments_list.html', takes_context=True)
def show_comment(context, post):
    # 获取当前post对象所关联的所有评论
    post_comments_list = post.comment_set.all()
    post_comments_count = post_comments_list.count()
    return {
        'post_comments_list': post_comments_list,
        'post_comments_count': post_comments_count,
    }