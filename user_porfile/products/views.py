from django.shortcuts import render
from .models import *


def product_detail_page(request,id):
    product = Product.objects.get(pk=id)
    d = {
        "product": product
    }
    return render(request, "products/detail.html", context=d) 