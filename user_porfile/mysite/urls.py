
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("profiles.urls")),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
    path("credit/", include("credit_system.urls"))
]
