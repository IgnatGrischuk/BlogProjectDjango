from django.shortcuts import render
from blog_app.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'posts': posts, "page": page})

