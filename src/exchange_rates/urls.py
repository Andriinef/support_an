from django.urls import path

from exchange_rates.api import get_price

urlpatterns = [
    path("price/", get_price, name="price"),
]
