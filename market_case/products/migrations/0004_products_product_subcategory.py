# Generated by Django 5.0.4 on 2024-04-19 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_category_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory'),
        ),
    ]