from django.db import models
from Product.models import Product
from seller.models import Seller

# Create your models here.
class Cart(models.Model):
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=0, max_digits=100000, default=0)

class CartItem(models.Model):
    quantity = models.DecimalField(decimal_places=0, max_digits=100)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(decimal_places=0, max_digits=100000)