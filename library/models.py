from unicodedata import category
from django.db import models


class AbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
  
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cover_pic = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    rating = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='books_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
