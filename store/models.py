from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User

#創建一個User模型，用來儲存購物的用戶
class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product, through='CartItem')

#創建一個Cart模型，用來儲存購物車中的商品及數量
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)

#創建一個CartItem模型，用來儲存購物車中的商品及數量
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product, through='OrderItem')
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

#創建一個OrderItem模型，用來儲存訂單中的商品及數量
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    
