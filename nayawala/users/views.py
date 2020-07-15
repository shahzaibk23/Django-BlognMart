from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from blogger.models import Blogger
from blogger.forms import BloggerModelForm


def signupPage(request):
    form = CreateUserForm(request.POST)
    form2 = BloggerModelForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == "POST":
            if form.is_valid():
                print("form1 is valid")
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name="blogger")
                user.groups.add(group)

                if form2.is_valid():
                    print("form2 is valid ")
                    picture = form2.cleaned_data.get("picture")
                    about = form2.cleaned_data.get('about')
                    Blogger.objects.create(
                    user=user,
                    username=username,
                    picture=picture,
                    about=about,
                        )

                    return redirect('login')

    context = {'form': form}
    return render(request, "t/signup.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {}
    return render(request, "t/login.html", context)

@login_required(login_url='login')
def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    context = {}
    return render(request, "t/blog.html", context)
