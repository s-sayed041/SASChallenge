from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    favorites = models.ManyToManyField('Item', related_name='favored_by')
    def __str__(self):
        return self.username
    
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name