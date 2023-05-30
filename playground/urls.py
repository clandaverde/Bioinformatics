from django.urls import path
from . import views

# URL configuration module (every app can have its own module)
urlpatterns = [
    path('index/', views.index),
    path('index/hello/', views.sendResult)
    
]