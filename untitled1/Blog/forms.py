from django import forms

from .models import Blog, Comment


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'picture',
            'summary',
        ]


class RawModelForm(forms.Form):
    cat_title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Category"}))


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
        ]