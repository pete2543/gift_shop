from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    price = models.IntegerField()
    total_product=models.IntegerField(default=0)
    content = models.TextField()
    img = models.ImageField(upload_to="img_product",blank=True)
    def __str__(self):
        return self.product_name
    
#class user(models.Model):
