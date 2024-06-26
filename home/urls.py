from django.urls import path

from home import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('contact/', views.contactpage, name='contact'),
    path('team/', views.teampage, name='team'),
    path('alljob/', views.jobpage, name='alljob'),
    path('post/', views.jobpostpage, name='post'),
    path('saveenquiry/', views.saveEnquiry,name='saveenquiry'),
     path('product/<int:id>/', views.product_details, name='productsDetails'),
]