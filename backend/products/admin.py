from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdminView(admin.ModelAdmin):
    fields = ["title", "content", "price"]


admin.site.register(Product, ProductAdminView)
