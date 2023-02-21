from django.urls import path

from online_store.views.base import products_view
from online_store.views.products import product_view, product_add_view, product_edit_view, product_delete_view
from online_store.views.categories import categories_view, category_view, category_add_view, category_edit_view, category_delete_view


urlpatterns = [
    path('', products_view, name='products'),
    path('products/', products_view, name='products'),

    path('products/<int:id>', product_view, name='product_detail'),
    path('products/add', product_add_view, name='product_add'),
    path('products/<int:id>/edit', product_edit_view, name='product_edit'),
    path('products/<int:id>/delete', product_delete_view, name='product_delete'),


    path('categories/', categories_view, name='categories'),

    path('categories/<int:id>', category_view, name='category_detail'),
    path('categories/add', category_add_view, name='category_add'),
    path('categories/<int:id>/edit', category_edit_view, name='category_edit'),
    path('categories/<int:id>/delete', category_delete_view, name='category_delete')
]
