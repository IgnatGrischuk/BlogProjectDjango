from django.urls import path
from blog_app.views import some_view


urlpatterns = [
    path('some-view/', some_view)
]
