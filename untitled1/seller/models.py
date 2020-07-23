from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    username = models.CharField(max_length=40)
    profile_pic = models.ImageField(blank=True)
    user = models.OneToOneField(User,null = True, blank=True,on_delete=models.CASCADE)

    def get_seller_url(self):
        from django.shortcuts import reverse
        return reverse("Seller:seller_details", kwargs={"seller_id": self.id})
