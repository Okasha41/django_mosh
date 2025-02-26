from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Collection


def say_hello(request):
    queryset = Product.objects.all()
    collection = Collection(pk=10)
    collection.featured_product = Product(pk=1)
    collection.save()
    return render(request, 'hello.html', {'name': 'Mosh', 'products': queryset})
