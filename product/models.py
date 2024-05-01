from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)

    name = models.CharField(max_length=255, verbose_name="Product Name")
    price = models.FloatField(verbose_name="Price")
    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return self.name
