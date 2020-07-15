from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

from .models import Blog, Comment, Category
from blogger.models import Blogger
from .forms import BlogModelForm, CommentModelForm, RawModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request):
    return render(request, "t/index.html", {})


def about_view(request):
    return render(request, "t/about.html", {})


@login_required(login_url='login')
def create_view(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    form2 = RawModelForm(request.POST)
    obj = Category.objects.all()
    if form.is_valid() and form2.is_valid():
        print("  hogyaa")
        form.save()
        t = form2.cleaned_data.get('cat_title')
        print("ye ha title")
        print(t)
        value = None
        for i in obj:
            print("yhn agyaa")
            if t == i.cat_title:
                print("agyaaaa")
                value = i
                print("value is", value)

        Blog.objects.create(
            title=form.cleaned_data.get('title'),
            picture=form.cleaned_data.get('picture'),
            summary=form.cleaned_data.get('summary'),
            content=form.cleaned_data.get('content'),
            category=value,
            blogger=request.user.blogger
        )

    context = {
        "title": form.fields['title'],
        "picture": form.fields['picture'],
        "summary": form.fields['summary'],
        "content": form.fields['content'],
        "obj": obj,
    }
    return render(request, "blogs/create.html", context)


def category_view(request, cat_id, *args, **kwargs):
    obj = get_object_or_404(Category, id=cat_id)
    obj2= obj.blog_set.all()
    context = {
        "obj":obj,
        "obj2":obj2,
    }
    return render(request, "t/category.html", context)


def single_blog_view(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Blog, id=my_id)
    obj2 = obj.comment_set.all()
    context = {
        "obj": obj,
        "obj2": obj2,
    }

    return render(request, "t/single-blog.html", context)

def blog_view(request):
    objs = Blog.objects.all()
    cat_objs = Category.objects.all()

    context = {
        "objs": objs,
        "cat_objs": cat_objs,
    }

    return render(request, "t/blog.html", context)


def product_list_view(request):
    return render(request, "t/product_list.html", {})


def single_list_view(request):
    return render((request, "t/single-procust.html", {}))


def login_view(request):
    return render(request, "t/login.html", {})


def checkout_view(request):
    return render(request, "t/checkout.html", {})


def cart_view(request):
    return render(request, "t/cart.html", {})


def confirmation_view(request):
    return render(request, "t/contact.html", {})


def elements_view(request):
    return render(request, "t/elements.html", {})


def comment_view(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Blog, id=my_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        form.save()
        Comment.objects.create(
            comment=form.cleaned_data.get('comment'),
            blogger=request.user.blogger,
            blog=obj
        )

    context = {
        "form": form,
        "obj": obj
    }

    return render(request, "t/comment.html", context)


def contact_view(request):
    return render(request, "t/contact.html", {})


def product_list(request):
    return render(request, "t/product_list.html", {})
