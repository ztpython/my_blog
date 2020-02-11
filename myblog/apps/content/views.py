from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.core.paginator import Paginator  # 实现分页

from .models import Post, Category, Tag

from django.views import View

import markdown  # markdown语法书写博文

# Create your views here.

# /page
class IndexView(View):
    def get(self, request, page=None):
        # 展示首页,按照最新创建时间列出所有文章
        # 如果没有传递页数,将首页数据返回
        if page is None:
            page = 1
        # 从数据库获取所有数据
        post_list = Post.objects.all()

        # 将这些数据1个为一页
        paginator = Paginator(post_list, 1)

        # 如果不是整数
        try:
            page = int(page)
        except Exception as e:
            page = 1
        # 如果大于最大
        if page > paginator.num_pages:
            pages = 1

        # 获取当前页的实例对象
        contents_page = paginator.page(page)

        # todo: 进行页码的控制，页面上最多显示3个页码
        # 1.总页数小于3页，页面上显示所有页码
        # 2.如果当前页是前2页，显示1-3页
        # 3.如果当前页是后2页，显示后3页
        # 4.其他情况，显示当前页的前1页，当前页，当前页的后1页
        num_pages = paginator.num_pages
        if num_pages < 3:
            pages = range(1, num_pages + 1)
        elif page <= 2:
            pages = range(1, 4)
        elif num_pages - page <= 1:
            pages = range(num_pages - 2, num_pages + 1)
        else:
            pages = range(page - 1, page + 2)

        # 组织上下文
        context = {
            'contents_page': contents_page,
            'pages': pages,
        }

        return render(request, 'index.html', context)

# /detail/post_id
class DetailView(View):
    def get(self, request, post_id):
        # 展示文章详情
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return redirect(reverse('content:index'))

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])

        post.body = md.convert(post.body)
        # 给post动态增加toc属性,标题
        post.toc = md.toc

        return render(request, 'detail.html', {'post':post})

# /archive/year/month/day
class ArchivesView(View):
    def get(self, request, year, month, day):
        # 根据选择的归档展示文章
        try:
            post_list = Post.objects.filter(create_time__year=year,
                                            create_time__month=month,
                                            create_time__day=day)
        except Post.DoesNotExist:
            return redirect(reverse('content:index'))
        return render(request, 'archive.html',{'post_list': post_list})

# /category/category_id
class CategoryView(View):
    def get(self, request, category_id):
        # 根据分类展示文章
        try:
            post_list = Post.objects.filter(category_id=category_id)
        except Post.DoesNotExist:
            return redirect(reverse('content:index'))
        return render(request, 'archive.html',{'post_list': post_list})

# /tag/tag_id
class TagView(View):
    def get(self, request, tag_id):
        # 根据标签云显示文章
        # try:
        #     tag = Tag.objects.filter(id=tag_id)
        # except Post.DoesNotExist:
        #     return redirect(reverse('content:index'))
        # print(tag)
        # post_list = Post.objects.filter(tags=tag)
        # print(post_list)
        tag = get_object_or_404(Tag, id=tag_id)
        print(tag)
        post_list = Post.objects.filter(tags=tag)
        print(post_list)
        return render(request, 'archive.html', {'post_list': post_list})