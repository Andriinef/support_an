import json

from django.http import JsonResponse

from exchange_rates.services import AlphavantageClient, AlphavantageResponse


def get_price(request):
    client = AlphavantageClient()
    return JsonResponse(
        AlphavantageResponse(**client.get_user_currency("USD", "UAH")).dict()
    )


def get_post_user(request):
    body = json.loads(request.body)
    from_currency = body["from"]
    to_currency = body["to"]
    client = AlphavantageClient()
    return JsonResponse(
        AlphavantageResponse(
            **client.get_user_currency(from_currency, to_currency)
        ).dict()
    )


# def get_post_user(request):
#     body = json.loads(request.body)
#     exchange_rates_request: ExchangeRatesInternalRequest(**body)
#     response: AlphavantageResponse = AlphavantageClient().fetch(exchange_rates_request)

#     return JsonResponse(response.dict())
