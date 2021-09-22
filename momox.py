import json
from typing import Optional

import requests
from requests.cookies import RequestsCookieJar

_HEADERS = {
    'X-API-TOKEN': '2231443b8fb511c7b6a0eb25a62577320bac69b6',
    'Content-Type': 'application/json',
    'X-MARKETPLACE-ID': 'momox_de'
}


def get_authentication_cookies(email: str, password: str) -> Optional[RequestsCookieJar]:
    response_options = requests.options('https://api.momox.de/api/v3/login/')

    login_data = {'email': email,
                  'password': password}
    response_login = requests.put('https://api.momox.de/api/v3/login/',
                                  headers=_HEADERS, data=json.dumps(login_data),
                                  cookies=response_options.cookies)

    if 400 <= response_login.status_code <= 499:
        print("HTTP error:",
              response_login.status_code,
              response_login.reason)
        return None

    return response_login.cookies


def query_offers(eans: list[str], authentication_cookies: RequestsCookieJar) -> list[float]:
    if authentication_cookies is None:
        print("Authentication cookies are required.")
        return []

    response = requests.get('https://api.momox.de/api/v4/quicksell/',
                            headers=_HEADERS, params={'eans': ','.join(eans)},
                            cookies=authentication_cookies)

    response_json = response.json()
    offers = [float(response_json[item]['price']) for item in response_json]
    return offers
