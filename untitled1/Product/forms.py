from django import forms
from .models import Product, Comments

class ProductModelFoem(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['seller', 'cat']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

class CategoryForm(forms.Form):
    cat_title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Category"}))