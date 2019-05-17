from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment, Category
from .forms import CommentForm

def blog_list(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 9)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/blog_list.html', context)

def blog_category(request, category):
    categories = Category.objects.all()
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(
        category__name__contains=category
    ).order_by(
        '-date_created'
    )
    paginator = Paginator(posts, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context)

def blog_post(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_post.html', context)
