from django.contrib import admin

from online_store.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'category', 'created_at', 'updated_at', 'price', 'image')
    list_filter = ('title', 'category')
    fields = ('title', 'description', 'category', 'price', 'image')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    list_filter = ('id', 'title')
    fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)
