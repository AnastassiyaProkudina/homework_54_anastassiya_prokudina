from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from online_store.models import Product, Category


def product_view(request, id):
    product = get_object_or_404(Product, pk=id)
    categories = Category.objects.all()
    return render(request, 'product.html', context={"product": product, 'categories': categories})

def product_add_view(request: WSGIRequest):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product_create.html', context={'categories': categories})
    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category_id': request.POST.get('category_id'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', id=product.id)


def product_edit_view(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product_edit.html', context={'product': product, 'categories': categories})
    product.title = request.POST.get('title')
    product.description = request.POST.get('description')
    product.category_id = request.POST.get('category_id')
    product.price = request.POST.get('price')
    product.image = request.POST.get('image')
    product.save()
    return redirect('product_detail', id=product.id)


def product_delete_view(request, id):
        data = get_object_or_404(Product, id=id)
        data.delete()
        return redirect('products')


