from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text']

    def clean_group(self):
        data = self.cleaned_data['group']
        group = Post.objects.filter(group=data)
        if not group.exists():
            raise forms.ValidationError('Такой группы не существует')
        return data