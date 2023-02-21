from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from online_store.models import Product, Category


def products_view(request: WSGIRequest):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'products.html', context=context)



