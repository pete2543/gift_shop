from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpRequest

def my_view(req):
    name = "Pete"
    age = 22
    return render(req,"index.html",{"name":name,"age":age})
