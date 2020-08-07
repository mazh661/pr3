from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from products.models import *
from orders.models import *

def profile_page(request):
    user = request.user
    orders = Order.objects.all().filter(user=user)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        address = request.POST['address']
        salary = request.POST['salary']
        profile.address = address
        profile.salary = salary
        profile.save()
        return redirect("profile_page")
    d = {
        "profile": profile,
        "orders": orders
    }
    return render(request, "profiles/profile.html", context=d)


def main_page(request):
    products = Product.objects.all()
    d = {
        "products":products
    }
    return render(request, "profiles/main.html", context=d)


def user_logout(request):
    logout(request)
    return redirect("main_page")



def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 and len(password) == 0:
            error = "Заполните все поля"
        elif len(username) == 0:
            error = "Заполните username"
        elif len(password) == 0:
            error = "Заполните password"
        else:
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is None:
                error = "нет такого пользователя"
            else:
                login(request, user)
                return redirect("main_page")
    d = {
        "error": error
    }
    return render(request, "profiles/login.html", context=d)


def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        address = request.POST['address']
        salary = int(request.POST['salary'])
        department_id = int(request.POST['department_id'])

        # create user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # get department
        department = Department.objects.get(pk=department_id)

        # create profile
        profile = Profile(user= user, department =department,
                          address=address, salary=salary)
        profile.save()
        return redirect("login_page")


    departments = Department.objects.all()
    d = {
        "departments": departments,
    }
    return render(request, "profiles/register.html", context=d)