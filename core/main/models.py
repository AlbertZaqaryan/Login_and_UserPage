from django.db import models
# Create your models here.


class Product(models.Model):
    
    # who = models.ForeignKey(on_delete=models.CASCADE, related_name='user_prod')
    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')

    def __str__(self):
        return self.name