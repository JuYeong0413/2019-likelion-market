from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path('', views.main, name="main"),
    path('<int:id>/', views.show, name="show"),
    path('favourite/', views.favourite, name="favourite"),
    path('<int:id>/like/', views.like, name="like"),
    path('<int:id>/unlike/', views.unlike, name="unlike"),
    path('buylist/', views.buylist, name="buylist"),
    path('single_order/', views.single_order, name="single_order"),
    path('order/', views.order, name="order"),
    path('cart_success/', views.cart_success, name="cart_success"),
    path('cart/', views.cart, name="cart"),
    path('cart_delete/', views.cart_delete, name="cart_delete"),
    path('write_review/', views.write_review, name="write_review"),
    path('create_review/', views.create_review, name="create_review"),
    path('review/', views.review, name="review"),
]