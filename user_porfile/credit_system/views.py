from django.shortcuts import render, redirect
from .models import *
def credit(request, product_id):
    credit_category = Credit_category.objects.all()
    d = {
        "product_id": product_id,
        "credit_category": credit_category
    }
    return render(request, "credit_system/credit.html", context=d)

def credit_action(request, product_id, credit_category_id):
    
    credit_category = Credit_category.objects.get(pk=credit_category_id) 
    product = Product.objects.get(pk=product_id)   
    user = request.user
    total_price = 1000
    accepted = True
    credit = Credit.objects.create(credit_category=credit_category, product=product, user=user, total_price=total_price, accepted=accepted)
    credit.save()
    return redirect("main_page")
