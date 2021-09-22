### Rebuy

Example code:

```python
from rebuy import query_offers

test_eans = ['3608964290', '9783608939842']
offers = query_offers(test_eans)
print(offers)

# Prints: [20.88, 12.19]
```


### Momox

Here an authentication is required to be able to access the API.

Example code:

```python
from momox import get_authentication_cookies, query_offers

test_eans = ['3608964290', '9783608939842']
cookies = get_authentication_cookies('your-email-address', 'your-password')
offers = query_offers(test_eans, cookies)
print(offers)

# Prints: [37.77, 10.46]
```
