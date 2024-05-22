from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_prod', blank=True)
    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')

    def __str__(self):
        return self.name