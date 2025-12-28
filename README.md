# -4
Blog应用程序设计
# Django 个人博客系统
这是一个基于Django框架开发的简易个人博客系统，实现了博客CRUD、分页展示、最新博客置顶、阅读量统计、权限控制等核心功能，适用于Python Web入门学习与实验展示。

## 项目功能
1.  **核心业务功能**
    -  博客增删改查（CRUD）：已登录用户可新建博客，仅博客作者可编辑/删除自身博客
    -  分页展示：博客列表按每页5篇进行分页，支持页码切换与上下页跳转
    -  最新置顶：博客按发布时间倒序展示，最新发布的博客自动置顶
    -  阅读量统计：非作者用户访问博客详情页后，阅读量自动累加，作者访问不统计
    -  权限控制：未登录用户仅可查看博客，新建/编辑/删除功能仅对已登录授权用户开放

2.  **后台管理功能**
    -  支持博客分类与博客文章的可视化管理
    -  可在后台直接添加、编辑、删除博客数据
    -  完整展示博客所有字段信息，数据操作实时生效


## 运行环境
-  Python 3.8+
-  Django 4.0+
-  操作系统：Windows/Mac/Linux

## 本地运行步骤
1.  **克隆项目**
    ```bash
    git clone https://github.com/chimamei/4.git
    cd 4
    安装依赖
    pip install django
    # 生成迁移文件（若未上传迁移文件时执行）
python manage.py makemigrations
# 执行迁移，创建数据库表
python manage.py migrate
python manage.py createsuperuser
# 按提示输入用户名、邮箱、密码
python manage.py runserver
