from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'post', 'author')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user' 'author')
    list_filter = ('pk',)
    empty_value_display = '-empty-'


admin.site.register(Follow)
