from django.contrib import admin
from store.models import Customer, Order, Product, OrderItem, ShippingAddress

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)