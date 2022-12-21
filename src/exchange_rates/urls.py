from django.urls import path

from exchange_rates.api import get_post_user, get_price

urlpatterns = [
    path("price/", get_price, name="price"),
    path("post_user/", get_post_user, name="get_post_user"),
]
