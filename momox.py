from typing import Optional

import requests

_HEADERS = {
    'X-API-TOKEN': '2231443b8fb511c7b6a0eb25a62577320bac69b6',
    'X-MARKETPLACE-ID': 'momox_de',
    'User-Agent': 'anything'
}


def _query_offer_for_single_ean(ean: str) -> Optional[float]:
    response = requests.get('https://api.momox.de/api/v4/media/offer/',
                            headers=_HEADERS, params={'ean': ean})
    json = response.json()
    if json['status'] != 'offer':
        return None
    return float(json['price'])


def query_offers(eans: list[str]) -> list[Optional[float]]:
    prices = list(map(_query_offer_for_single_ean, eans))
    return prices
