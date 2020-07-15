from django import forms

from .models import Blogger


class BloggerModelForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields =[
            'picture',
            'about',
        ]