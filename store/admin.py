from django.contrib import admin

# Register your models here.
from .models import Product,Cart, CartItem, Order, OrderItem

admin.site.register(Product)

class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
#功能：显示购物车的详细信息
class OrderItemInline(admin.TabularInline):
    model = OrderItem
#功能：显示订单的详细信息
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

