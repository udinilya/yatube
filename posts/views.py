from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import datetime
from .models import Post, Group, Comment, Follow
from .forms import PostForm, CommentForm
from users.forms import User


def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'paginator': paginator})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'group.html', {'group': group, 'page': page, 'paginator': paginator})


def morning(request):
    latest = Post.objects.filter(
                 text__contains='утро'
             ).filter(
                 author=2
             ).filter(
                 pub_date__range=(datetime.date(1854, 7, 7), datetime.date(1854, 7, 21))
             )
    return render(request, 'index.html', {'posts': latest})


def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = Post(text=form.cleaned_data['text'], group=form.cleaned_data['group'])
                post.author = request.user
                post.save()
                return redirect('index')
            return render(request, 'new_post.html', {'form': form})
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})
    else:
        return redirect('/auth/login')


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author).order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    if request.user.is_authenticated:
        following = Follow.objects.filter(user=request.user, author=author)
    else:
        following = False
    return render(request, 'profile.html', {'author': author, 'page': page, 'paginator': paginator, 'post_list': post_list,
                                            'following': following})


def post_view(request, username, post_id):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, author=user, id=post_id)
    post_list = Post.objects.filter(author=user).order_by('-pub_date').all()
    comments = post.comments.order_by('-created').all()
    form = CommentForm()
    return render(request, 'post.html', {'post': post, 'comments': comments, 'form': form, 'post_list': post_list})


@login_required
def post_edit(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return redirect('post', post.author, post_id)

    if request.method == 'POST':
        form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
        if form.is_valid():
            post.save()
        return redirect('post', username, post_id)
    else:
        form = PostForm(instance=post)

    return render(request, 'new_post.html', {'form': form, 'post': post})


@login_required
def add_comment(request, username, post_id):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, author=user, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(text=form.cleaned_data['text'])
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return redirect('post', username, post_id)
        else:
            form = CommentForm()
        return render(request, 'comments.html', {'form': form})
    form = CommentForm()
    return render(request, 'comments.html', {'form': form, 'user': user, 'post': post})


@login_required
def follow_index(request):
    post_list = Post.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'follow.html', {'page': page, 'paginator': paginator})


@login_required
def profile_follow(request, username):
    user = request.user
    author = User.objects.get(username=username)
    follower = Follow.objects.filter(user=user, author=author)
    if user != author and not follower.exists():
        Follow.objects.create(user=user, author=author)
    return redirect('profile', author.username)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    follower = Follow.objects.filter(user=request.user, author=author)
    if follower.exists():
        follower.delete()
    return redirect('profile', username=author)


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
