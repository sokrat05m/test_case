from django.contrib import admin

from cart.models import Cart, CartItem


# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ['id', 'user']
    list_display = ['id', 'user']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    fields = ['id', 'product', 'quantity', 'cart']
    list_display = ['id', 'product', 'quantity', 'cart']
