from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    img = models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_all_product():
       return Product.objects.all()
    
    @staticmethod
    def get_all_product_by_category(category_id):
        return Product.objects.filter(category=category_id)

    @staticmethod
    def get_product_by_id(id):
        return Product.objects.filter(id=id)

    @staticmethod
    def get_cart_products_by_id(ids):
        return Product.objects.filter(id__in=ids)