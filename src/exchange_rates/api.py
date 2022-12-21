import json
from django.http import JsonResponse
from exchange_rates.services import (
    AlphavantageResponse,
    PriceClient,
)


def get_price(request):
    client = PriceClient()
    return JsonResponse(
        AlphavantageResponse(
            **client.get_user_currency("USD", "UAH")
        ).dict()
    )


def get_post_user(request):
    body = json.loads(request.body)
    from_currency = body["from"]
    to_currency = body["to"]
    client = PriceClient()
    return JsonResponse(
        AlphavantageResponse(
            **client.get_user_currency(from_currency, to_currency)
        ).dict()
    )
