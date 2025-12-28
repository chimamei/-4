from django.contrib import admin
from .models import BlogPost, BlogCategory  # 新增导入BlogCategory

# 注册分类模型和博客模型
admin.site.register(BlogCategory)
admin.site.register(BlogPost)