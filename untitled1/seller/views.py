from django.shortcuts import render, get_object_or_404
from .models import Seller


# Create your views here.

def sellerDetailsPage(request, seller_id, *args, **kwargs):
    obj = get_object_or_404(Seller, id=seller_id)
    prods = obj.product_set.all()


    l = enumerate(prods)
    context = {
        "obj":obj,
        "prod":prods,
        "l":l,
    }
    return render(request, "seller/index.html", context)
