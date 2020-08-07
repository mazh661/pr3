
from django.urls import path
from .views import *
urlpatterns = [
    path("credit/<int:product_id>", credit, name="credit"), 
    path("credit_action/<int:product_id>/<int:credit_category_id>/", credit_action, name="credit_action")

]