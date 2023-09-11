from django.contrib.auth import login , logout
from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpRequest,HttpResponseRedirect
from .models import Product
from django.urls import reverse
from myapp.forms import RegisterFrom
def my_view(req):
    product = Product.objects.all()
    
    return render(req,"index.html",{"product":product})

def register (req:HttpRequest):
    if req.method == "POST":
        form = RegisterFrom(req.POST)
        if form.is_valid():
            user= form.save()
            login(req,user)
            return HttpResponseRedirect(reverse("index"))#login แล้วกลับไปที่หน้าhomeได้เลย
    else:
        form = RegisterFrom()
    #GET 
    context = {"form":form}
    return render(req,"app_users/register.html",context)