from django.urls import path

from home import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('contact/', views.contactpage, name='contact'),
    path('team/', views.teampage, name='team'),
    path('productsDetails/', views.productpage, name='productsDetails'),

]