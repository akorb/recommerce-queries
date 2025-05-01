from typing import Optional
import requests


def get_price_from_response(json_response: dict, ean: str) -> Optional[float]:
    for purchsable in json_response['purchasable']:
        if ean in purchsable['product']['identifiers_ean'] or \
           ean in purchsable['product']['identifiers_isbn']:
            return purchsable['product']['price_purchase'] / 100

    return None


def query_offers(eans: list[str]) -> list[Optional[float]]:
    response = requests.post('https://www.rebuy.de/verkaufen/api/bulk-isbn',
                             json={'identifiers': "\r\n".join(eans)},
                             headers={'X-Requested-With': 'XMLHttpRequest'})

    json: dict = response.json()

    prices = [get_price_from_response(json, ean) for ean in eans]
    return prices
