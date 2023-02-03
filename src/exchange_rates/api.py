import json

from django.http import JsonResponse

from exchange_rates.services import AlphavantageClient, AlphavantageResponse

# def get_price(request):
#     client = AlphavantageClient()
#     return JsonResponse(
#         AlphavantageResponse(**client.get_user_currency("USD", "UAH")).dict()
#     )


def get_price(request) -> JsonResponse:
    if request.method == "POST":
        body: dict = json.loads(request.body)
        from_currency: str = body["from"]
        to_currency: str = body["to"]
    elif request.method == "GET":
        from_currency: str = "USD"
        to_currency: str = "UAH"
    responce = AlphavantageResponse(**AlphavantageClient().get_user_currency(from_currency, to_currency))
    return JsonResponse(responce.dict())


# def get_post_user(request):
#     body = json.loads(request.body)
#     exchange_rates_request: ExchangeRatesInternalRequest(**body)
#     response: AlphavantageResponse = AlphavantageClient().fetch(exchange_rates_request)

#     return JsonResponse(response.dict())
