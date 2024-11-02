from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        id=id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.select_related(
        'category',
        'location',
        'author').filter(
        is_published=True, pub_date__lte=timezone.now(),
        category__is_published=True)
    return render(request, 'blog/category.html',
                  {'category': category,
                   'post_list': post_list})
