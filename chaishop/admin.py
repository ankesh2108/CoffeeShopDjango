from django.contrib import admin

# Register your models here.
from .models.customer import Customer
from .models.product import Product
from .models.category import Category
from .models.order import Order

class AdminProduct(admin.ModelAdmin):
   list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)