from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ec/', views.ec, name='ec'),
    path('events/', views.events, name='events'),
    path('articles/', views.articles, name='articles'),
]