from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from online_store.models import Category


def categories_view(request: WSGIRequest):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'categories.html', context=context)
    data = get_object_or_404(Category, id=id)
    data.delete()
    return redirect('categories')

def category_view(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'category.html', context={"category": category})

def category_add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'category_create.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }
    category = Category.objects.create(**category_data)
    return redirect('category_detail', id=category.id)

def category_edit_view(request: WSGIRequest, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        return render(request, 'category_edit.html', context={'category': category})
    category.title = request.POST.get('title')
    category.description = request.POST.get('description')
    category.save()
    return redirect('category_detail', id=category.id)


def category_delete_view(request, id):
        data = get_object_or_404(Category, id=id)
        data.delete()
        return redirect('categories')
