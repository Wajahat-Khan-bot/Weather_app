from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'), #the path for our index view
]