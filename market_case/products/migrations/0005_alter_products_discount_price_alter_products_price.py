# Generated by Django 5.0.4 on 2024-04-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount_price',
            field=models.IntegerField(verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена товара'),
        ),
    ]
