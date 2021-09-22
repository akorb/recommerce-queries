import requests

from pyquery import PyQuery


def get_token() -> tuple[str, str]:
    response = requests.get('https://www.rebuy.de/verkaufen/bulk-isbn')
    html = response.text
    pq = PyQuery(html)

    search_token = pq('#isbn_product_search__token')[0].value
    php_session_id = response.cookies['PHPSESSID']
    return search_token, php_session_id


def query_offers(eans: list[str], token=get_token()) -> list[float]:
    search_token, php_session_id = token
    data = {'isbn_product_search[identifiers]': "\r\n".join(eans),
            'isbn_product_search[_token]': search_token}

    response = requests.post('https://www.rebuy.de/verkaufen/bulk-isbn',
                             data=data,
                             cookies={'PHPSESSID': php_session_id})

    html = response.text
    pq = PyQuery(html)

    offers = [float(elem.text.strip().split()[0].replace(',', '.'))
              for elem in pq('div[class="pull-right ry-cart-item__price ry-cart-item__price--bulk-isbn-result"]')]
    return offers
