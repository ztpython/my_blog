from django import template

from apps.content.models import Post, Category, Tag
# 使用自定义模板标签,实现生成最新文章, 标签, 归档, 分类
register = template.Library()

# 实现生成最新文章
@register.inclusion_tag('content/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=3):
    return {
        'recent_post_list': Post.objects.all().order_by('-create_time')[:num],
    }

# 实现归档
@register.inclusion_tag('content/inclusions/_archives.html', takes_context=True)
def show_date(context):
    return {
        'date_list': Post.objects.dates('create_time', 'day', order='DESC')
    }

# 实现分类
@register.inclusion_tag('content/inclusions/_category.html', takes_context=True)
def show_category(context):
    return {
        'category_list': Category.objects.all()
    }

# 实现生成标签
@register.inclusion_tag('content/inclusions/_show_tags.html', takes_context=True)
def show_tags(context):
    return{
        'tag_list': Tag.objects.all()
    }
