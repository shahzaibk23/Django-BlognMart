from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Comments, Categories

from .forms import ProductModelFoem, CommentModelForm, CategoryForm

from cart.forms import CartItemForm
from cart.models import CartItem, Cart

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def create_view(request, *args, **kwargs):

    form = ProductModelFoem(request.POST, request.FILES)
    form2 = CategoryForm(request.POST)
    cats = Categories.objects.all()

    context = {
        "form":form,
        "form2":form2,
        "cats":cats
    }

    if form.is_valid() and form2.is_valid():
        Product.objects.create(
            title = form.cleaned_data.get('title'),
            desc = form.cleaned_data.get('desc'),
            price = form.cleaned_data.get('price'),
            summary = form.cleaned_data.get('summary'),
            pic = form.cleaned_data.get('pic'),
            cat = Categories.objects.get(title=form2.cleaned_data.get("cat_title")),
            displayImage1 = form.cleaned_data.get('displayImage1'),
            displayImage2 = form.cleaned_data.get('displayImage2'),
            displayImage3 = form.cleaned_data.get('displayImage3'),
            seller = request.user.seller
        )
        return redirect('product_list')
    #     print("------------------VALIDATED")
    # else:
    #     print("-----------------ERROR")

    return render(request, "product/index.html", context)

def comment_view(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Product, id = my_id)
    form = CommentModelForm(request.POST)

    if form.is_valid():
        Comments.objects.create(
            content=form.cleaned_data.get('content'),
            user = request.user.seller,
            product = obj
        )
        return redirect('Product:prod_details', my_id=obj.id)
    context = {
        "form":form,
        "obj":obj
    }
    return render(request, "t/comment_product.html", context)

def addToCartView(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Product, id=my_id)
    cartForm = CartItemForm(request.POST)
    cartObjs = CartItem.objects.all()
    v = 0
    for i in cartObjs:
        if i.product == obj:
            v = 1
            break
    if cartForm.is_valid():
        if cartForm.cleaned_data.get('quantity') > 0 and v == 0:
            c = Cart.objects.get(seller=request.user.seller)
            CartItem.objects.create(
                quantity=cartForm.cleaned_data.get('quantity'),
                product=obj,
                cart = c,
                total= cartForm.cleaned_data.get('quantity') * obj.price,
            )

            return redirect("cart")
    context = {
        "obj": obj,
        "form":cartForm
    }
    return render(request, "t/addToCart.html", context)

def category_view(request, cat_id, *args, **kwargs):
    obj = get_object_or_404(Categories, id = cat_id)
    prods = obj.product_set.all()
    cats = Categories.objects.all()
    context={
        "obj":obj,
        "prods":prods,
        "cats":cats
    }
    return render(request, "t/category.html", context)