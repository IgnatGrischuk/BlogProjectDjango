from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('tags/<tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('by_author/<author>', views.posts_by_author, name='posts_by_author')
]
