from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "status")


admin.site.register(Product, ProductAdmin)

