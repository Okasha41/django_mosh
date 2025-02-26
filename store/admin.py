from django.contrib import admin
from . import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price','inventory_status', 'collection_status']
    ordering = ['title']
    list_select_related = ['collection']

    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    def collection_status(self, product):
        return product.collection.title
