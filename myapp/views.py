from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpRequest
from .models import Product
def my_view(req):
    product = Product.objects.all()
    
    return render(req,"index.html",{"product":product})
