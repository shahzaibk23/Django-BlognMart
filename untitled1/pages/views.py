from django.shortcuts import render, get_object_or_404
from Product.models import Product, Categories
from cart.forms import CartItemForm
from cart.models import Cart
# Create your views here.

def home_view(request):
    return render(request, "t/HOME.html",{})

def about_view(request):
    return render(request, "t/about.html",{})

def blog_view(request):
    return render(request, "t/blog.html", {})

def product_list_view(request):
    cats = Categories.objects.all()
    objs = Product.objects.all()
    context = {
        "objs" : objs,
        "cats":cats
    }
    return render(request, "t/product_list.html", context)

def single_list_view(request, my_id, *args, **kwargs):
    # cartForm = CartItemForm(request.POST)
    obj = get_object_or_404(Product, id = my_id)
    commentObj = obj.comments_set.all()
    # if cartForm.is_valid():
    #    CartItem.objects.create(
    #        quantity=cartForm.cleaned_data.get('quantity'),
    #        product=obj
    #    )
    context = {
        "obj":obj,
        "com":commentObj,
        # "form":cartForm
    }
    return render(request, "t/single-product.html", context)

def login_view(request):
    return render(request, "t/login.html", {})

def checkout_view(request):
    obj = Cart.objects.get(seller=request.user.seller)
    t = obj.total + 100

    prodObjs = obj.cartitem_set.all()
    context = {
        "obj": obj,
        'prods': prodObjs,
        "t":t
    }

    return render(request, "t/checkout.html", context)

def cart_view(request):
    obj = Cart.objects.get(seller = request.user.seller)
    prodObjs = obj.cartitem_set.all()
    t = 0
    for i in prodObjs:
        t += i.total
    obj.total = t
    obj.save()
    context = {
        "obj" : obj,
        'prods':prodObjs
    }
    return render(request, "t/cart.html",context)

def confirmation_view(request):
    return render(request, "t/contact.html", {})

def elements_view(request):
    return render(request, "t/elements.html", {})

def single_blog_view(request):
    return render(request, "t/single-blog.html", {})

def contact_view(request):
    return render(request, "t/contact.html", {})

# def product_list(request):
#     objs = Product.objects.get( id =1 )
#     print("--------------------------------------",objs.title)
#     context = {
#         "objs":objs
#     }
#     return render(request, "t/product_list.html", context)