from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=20)

    def get_category():
        return Category.objects.all()
    def get_category_name(id):
        return Category.objects.filter(id=id)