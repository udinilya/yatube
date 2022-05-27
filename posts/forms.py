from django import forms
from .models import Post, Group


class PostForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    text = forms.CharField(widget=forms.Textarea)

    def clean_group(self):
        data = self.cleaned_data['group']
        group = Post.objects.filter(group=data)
        if not group.exists():
            raise forms.ValidationError('Такой группы не существует')
        return data
