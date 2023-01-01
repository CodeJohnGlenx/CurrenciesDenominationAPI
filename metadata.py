"""
metadata.py

- contains the metadata of the API
"""

app_title="Currency Denomination API"
description = """The conversion between two currencies and the nearest denomination of the converted currency.
## Accepted Currencies 
[PHP, USD, EUR, AUD, JPY]

## Example Usage
* https.../denomination?currency_from=PHP&currency_to=USD&from_value=315.75

### returns
* {"from":"PHP","to":"USD","exchange_rate":0.017969,"date":"2023-01-01","from_value":315.75,"to_value":5.67,"to_denomination":{"5":1,"0.50":1,"0.10":1,"0.05":1,"0.01":2}}
"""
version="1.0.pogi"

tags_metadata = [
    {
        "name": "currency_from",
        "description": "Currency code to convert from. Accepted currency codes at the moment [PHP, USD, EUR, AUD, JPY]",
    },
    {
        "name": "currency_to",
        "description": "Currency code to convert to. Accepted currency codes at the moment [PHP, USD, EUR, AUD, JPY]",
    },
    {
        "name": "from_value",
        "description": "Positive float value of currency_from",
    },
    {
        "name": "pogi",
        "description": "Ang pogi po ni John Glen Falceso",
    },
]
