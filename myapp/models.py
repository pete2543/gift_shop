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
    #user_name = models.CharField(max_length=128,unique=True)
    #First_name = models.CharField(max_length=128)
    #Last_name = models.CharField(max_length=128)
    #password  = models.CharField(max_length=128)
    #email = models.EmailField(unique=True)
    #def __str__(self):
       # return self.user_name