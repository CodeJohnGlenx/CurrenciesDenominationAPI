# CurrenciesDenominationAPI
The conversion between two currencies and the nearest denomination of the converted currency. Accepted currencies at the moment are PHP, USD, EUR, AUD, JPY. 

## Accepted Currencies 
[PHP, USD, EUR, AUD, JPY]

## Example Usage
* https://currency-denomination-api.onrender.com/denomination?currency_from=PHP&currency_to=USD&from_value=315.75&available_denomination=all
* returns ```{"from":"PHP","to":"USD","exchange_rate":0.017969,"date":"2023-01-01","from_value":315.75,"to_value":5.67,"to_denomination":{"5":1,"0.50":1,"0.10":1,"0.05":1,"0.01":2}}```

* https://currency-denomination-api.onrender.com/denomination?currency_from=PHP&currency_to=USD&from_value=315.75&available_denomination=[20,5,0.25]
* returns ```{"from":"PHP","to":"USD","exchange_rate":0.018264,"date":"2023-02-13","from_value":315.75,"to_value":5.77,"to_denomination":{"20":0,"5":1,"0.25":3}}```

## Docs
check out our documentation here:
https://currency-denomination-api.onrender.com/docs