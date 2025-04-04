from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new',views.new),
    path('vivo20',views.vivo20),
    path('hemanth', views.hemanth)
]