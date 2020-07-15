# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
from blogger.models import Blogger


class Category(models.Model):
    cat_title = models.CharField(max_length=120)

    def get_cat_url(self):
        return reverse("Blog:category", kwargs={"cat_id":self.id})


class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    picture = models.ImageField()
    summary = models.TextField()
    datetime = models.DateTimeField(default=timezone.now, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("Blog:blogDetails", kwargs={"my_id": self.id})


    def comment_url(self):
        return reverse("Blog:comment", kwargs={"my_id": self.id})


class Comment(models.Model):
    comment = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

