from django.urls import path
from exchange_rates.api import get_price, get_post_user


urlpatterns = [
    path("price/", get_price, name="price"),
    path("post_user/", get_post_user, name="get_post_user"),
]
