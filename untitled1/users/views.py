from django.shortcuts import render, redirect
from seller.forms import CreateSellerForm

# Create your views here.
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from seller.models import Seller
from django.contrib.auth import authenticate, login, logout
from cart.models import Cart
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm(request.POST)
        form2 = CreateSellerForm(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name  = 'seller')
                user.groups.add(group)


                if form2.is_valid():
                    s = Seller.objects.create(
                        user = user,
                        username = username,
                        profile_pic = form2.cleaned_data.get('profile_pic')
                    )
                    Cart.objects.create(
                        seller = s
                    )

                    return redirect('login')
    context = {
        "form":form,
        "fomr2":form2
    }
    return render(request, "t/signup.html", context)

def login_view(request):
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


    return render(request, "t/login.html", {})