from django.db import models
from django.contrib.auth.models import User

# 博客分类模型（无修改，保留完整）
class BlogCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = "博客分类"


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="博客标题")
    text = models.TextField(verbose_name="博客正文")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="博客分类")
    # 新增：阅读量字段
    read_count = models.PositiveIntegerField(default=0, verbose_name="阅读量")

    def __str__(self):
        return self.title[:50]

    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"