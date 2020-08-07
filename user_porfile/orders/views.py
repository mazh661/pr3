from django.shortcuts import render, redirect
from products.models import *
from .models import *
# Create your views here.
def order(request):
    if request.method == "POST":
        user = request.user
        product = Product.objects.get(pk=int(request.POST['product_id']))
        count = request.POST['count']
        order = Order.objects.create(user=user,product=product, count=count)
        order.save()
    return redirect("main_page")