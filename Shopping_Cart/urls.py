
from django.urls import path,include
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.my_view,name ='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('Shopping_Cart/', views.register, name='Shopping_Cart'),
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='your_custom_login.html'), name='login'),
]
