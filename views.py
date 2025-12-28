from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import models
from .models import BlogPost
from .forms import BlogPostForm

# 首页视图（完整修改版：按发布时间倒序，实现最新博客置顶）
def index(request):
    # 按发布时间倒序排列，最新博客自动在顶部
    blog_post_list = BlogPost.objects.all().order_by('-date_added')
    paginator = Paginator(blog_post_list, 5)
    page_number = request.GET.get('page', 1)
    blog_posts = paginator.get_page(page_number)
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)

# 其他视图（无修改，保留完整，确保文件正常运行）
@login_required
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            messages.success(request, '博客创建成功！')
            return redirect('index')
    else:
        form = BlogPostForm()

    context = {'form': form, 'title': '新建博客'}
    return render(request, 'blogs/post_form.html', context)

@login_required
def edit_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)

    if blog_post.owner != request.user:
        messages.error(request, '你没有权限编辑这篇博客！')
        return redirect('index')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, '博客编辑成功！')
            return redirect('index')
    else:
        form = BlogPostForm(instance=blog_post)

    context = {'form': form, 'title': '编辑博客', 'blog_post': blog_post}
    return render(request, 'blogs/post_form.html', context)

# 博客详情视图（完整修改版：新增阅读量计数逻辑）
def post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    # 阅读量+1（排除作者自己访问，避免自刷）
    if not request.user.is_authenticated or request.user != blog_post.owner:
        blog_post.read_count += 1
        blog_post.save()
    context = {'blog_post': blog_post}
    return render(request, 'blogs/post_detail.html', context)

@login_required
def delete_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    if blog_post.owner != request.user:
        messages.error(request, '你没有权限删除这篇博客！')
        return redirect('index')
    blog_post.delete()
    messages.success(request, '博客删除成功！')
    return redirect('index')

def search_post(request):
    keyword = request.GET.get('keyword', '').strip()
    blog_posts = []
    if keyword:
        blog_posts = BlogPost.objects.filter(
            models.Q(title__icontains=keyword) | models.Q(text__icontains=keyword)
        ).order_by('-date_added')
    context = {'blog_posts': blog_posts, 'keyword': keyword}
    return render(request, 'blogs/index.html', context)