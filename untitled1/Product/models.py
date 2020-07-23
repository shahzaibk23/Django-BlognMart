from django.db import models
from seller.models import Seller
from django.shortcuts import reverse

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=30)

    def get_cat_url(self):
        return reverse("Product:category", kwargs={"cat_id":self.id})

class Product(models.Model):
    title = models.CharField(max_length=30, default="")
    desc = models.TextField(default="")
    price = models.DecimalField(decimal_places=0, max_digits=10000, default=0)
    summary = models.TextField(default="")
    pic = models.ImageField()
    cat = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    displayImage1 = models.ImageField(blank=True, null=True)
    displayImage2 = models.ImageField(blank=True, null=True)
    displayImage3 = models.ImageField(blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):

        return reverse("Product:prod_details", kwargs={"my_id": self.id})

    def get_comment_url(self):
        return reverse("Product:comment", kwargs={"my_id":self.id})

    def get_cart_url(self):
        return reverse("Product:add_to_cart", kwargs={"my_id": self.id})


class Comments(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.SET_NULL, null = True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="")

