from django.shortcuts import render, get_object_or_404
import datetime
from .models import Post, Group


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
