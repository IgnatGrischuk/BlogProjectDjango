from django import forms
from blog_app.models import Post
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')
