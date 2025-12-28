from django.urls import path
from . import views

urlpatterns = [
    # 原有正常路由（保留不变）
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    # 关键修复：确保该路由存在，名称与模板一致，无拼写错误
    path('search/', views.search_post, name='search_post'),
]