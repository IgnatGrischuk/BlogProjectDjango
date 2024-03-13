from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_edit/<int:post_id>', views.post_edit, name='post_edit'),
    path('tags/<tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('author/<int:author_id>/', views.posts_by_author,
         name='posts_by_author'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]
