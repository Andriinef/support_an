import pydantic
import requests
from django.conf import settings
from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    # from_currency: str = Field(alias="1. From_Currency Code")
    # to_currency: str = Field(alias="3. To_Currency Code")
    rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


class ExchangeRatesInternalRequest(BaseModel):
    from_: str = pydantic.Field(alias="from")
    to: str


class AlphavantageClient:
    def _get(self, query, params):
        return requests.get(
            f"{settings.ALPHA_VANTAGE_BASE_URL}/{query}",
            params={
                "apikey": settings.ALPHA_VANTAGE_API_KEY,
                **params,
            },
        )

    def get_user_currency(self, from_currency, to_currency):
        response = self._get(
            "query",
            params={
                "function": "CURRENCY_EXCHANGE_RATE",
                "from_currency": from_currency,
                "to_currency": to_currency,
            },
        )
        return response.json()
