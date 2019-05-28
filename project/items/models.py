from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class Item(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
    
    bought = models.IntegerField(default=0)
    favourites = models.ManyToManyField(User, related_name='favourites')
    cart = models.ManyToManyField(User, related_name='cart')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(Item, related_name='order_items')
    total_price = models.IntegerField(default=0)
    review_written = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def reviews(self):
    #     return Review.objects.filter(order=self)
    
    
class Review(models.Model):
    objects = models.Manager()
    content = models.TextField()
    star = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    