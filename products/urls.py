
from django.urls import path
from .views import *
urlpatterns = [
    path("detail/<int:id>/", product_detail_page, name="product_detail_page")
]
