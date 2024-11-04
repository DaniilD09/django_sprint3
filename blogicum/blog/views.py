from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def posts():
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    return render(request, 'blog/index.html', {'post_list': posts()[:5]})


def post_detail(request, post_id):
    post = get_object_or_404(posts(), id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(request, 'blog/category.html',
                  {'category': category,
                   'post_list': posts().filter(category=category)})

# Привет я оставил [:5] и в models.py TEXT_LENGTH = 256, правильно ли понимаю,
# что мне нужно сделать отдельный файл с константами и туда их все запихнуть а
# потом их наследовать?
