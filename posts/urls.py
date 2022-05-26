from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('morning/', views.morning),
    path('group/<slug>/', views.group_posts),
]
