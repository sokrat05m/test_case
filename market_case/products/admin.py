from django.contrib import admin

from products.models import Product, Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']
    list_display = ['category_name']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    fields = ['subcategory_name', 'parent']
    list_display = ['subcategory_name', 'parent']


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name',
              'price',
              'discount_price',
              'product_balance',
              'product_characteristics',
              'product_category',
              'product_subcategory']
    list_display = ['product_name',
                    'price',
                    'discount_price',
                    'product_balance',
                    'product_characteristics',
                    'product_category',
                    'product_subcategory']
