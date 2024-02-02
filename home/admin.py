from django.contrib import admin
from .models import Category, Product, MyCart, OrderPlaced, Contact, SubscriptionEmail
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight','available_quantity', 'selling_price', 'return_policy', 'tags', 'modified_date']

@admin.register(MyCart)
class MyCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'date_created']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'total_price', 'ordered_date', 'order_status']

    def customer_info(self, obj):
        link = reverse('admin:registration_customer_change', args=[obj.customer.id])
        return format_html('<a href="{}">{}</a>', link, obj.customer.full_name)

    def product_info(self, obj):
        link = reverse('admin:home_product_change', args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', link, obj.product.name)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['sno', 'full_name', 'email', 'message', 'created_at']
    
@admin.register(SubscriptionEmail)
class SubscriptionEmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'subscribed_at']