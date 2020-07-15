from django.db import models
from django.contrib.auth.models import User


class Blogger(models.Model):
    username = models.CharField(max_length=30, default="")
    picture = models.ImageField(null=True)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
