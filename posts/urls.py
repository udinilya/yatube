from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('morning/', views.morning),
    path('group/<slug>/', views.group_posts),
    path('new/', views.new_post, name='new_post'),
]
