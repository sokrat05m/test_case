from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=255)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    product_name = models.CharField(max_length=255,
                                    verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара')
    discount_price = models.IntegerField(verbose_name='Цена со скидкой')
    product_balance = models.IntegerField()
    product_characteristics = models.TextField()
    product_category = models.ForeignKey(Category,
                                         on_delete=models.CASCADE,
                                         null=True)
    product_subcategory = models.ForeignKey(Subcategory,
                                            on_delete=models.CASCADE,
                                            null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
