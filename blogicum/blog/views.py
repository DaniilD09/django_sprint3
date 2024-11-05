from django.shortcuts import get_object_or_404, render

from .models import Category, Post
from blogicum.constants import POST_PER_PAGE


def index(request):
    return render(
        request,
        'blog/index.html',
        {'post_list': Post.published_objects.all()[:POST_PER_PAGE]}
    )


def post_detail(request, post_id):

    return render(
        request,
        'blog/detail.html',
        {'post': get_object_or_404(Post.published_objects.all(),
         id=post_id)}
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(
        request,
        'blog/category.html',
        {'category': category,
         'post_list': Post.published_objects.filter(category=category)})
