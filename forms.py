from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """基于BlogPost模型创建的表单，用于新建和编辑博客"""
    class Meta:
        model = BlogPost
        # 新增 category 字段
        fields = ['title', 'category', 'text']
        # 自定义字段标签
        labels = {
            'title': '博客标题',
            'category': '博客分类',  # 新增分类标签
            'text': '博客正文'
        }