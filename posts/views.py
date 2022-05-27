from django.shortcuts import render, get_object_or_404, redirect
import datetime
from .models import Post, Group
from .forms import PostForm


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


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
