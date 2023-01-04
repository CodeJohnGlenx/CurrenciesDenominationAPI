from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import regex
import math 
import metadata

app = FastAPI(openapi_tags=metadata.tags_metadata, title=metadata.app_title, version=metadata.version, description=metadata.description)

# cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

accepted_currencies = ['PHP', 'USD', 'AUD', 'EUR', 'JPY']  
output = {
    'from': None, 
    'to': None, 
    'exchange_rate': None, 
    'date': None, 
    'from_value': None, 
    'to_value': None, 
    'to_denomination': None,
}

# home page
@app.get("/", tags=['pogi'])
def read_root():
    return {"pogi": "John Glen Falceso"}


# denomination page
@app.get("/denomination", tags=['currency_from', 'currency_to', 'from_value'])
def convert_denomination(currency_from: str, currency_to: str, from_value: float):
    try:

        # currency_from or currency_to not in accepted_currencies
        if not (currency_from in accepted_currencies):
            raise ValueError(f'currency to not in accepted currencies: {accepted_currencies}')

        if not (currency_to in accepted_currencies):
            raise ValueError(f'currency to not in accepted currencies: {accepted_currencies}')
        
        # from value is negative
        if from_value < 0:
            raise ValueError(f'negative from_value')

        convert_currency(currency_from.upper(), currency_to.upper(), from_value)
        output['to_denomination'] = regex.get_denomination(regex.currencies[output['to']], output['to_value'])
        
    except ValueError as e:
        return {'error': e.args[0]}
    except Exception as e:
        return {'error': e}

    return output


# get the conversion between from currency and to currency 
def convert_currency(currency_from, currency_to, currency_from_value):
    if currency_from in accepted_currencies and currency_to in accepted_currencies:
        url = f"https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}"

        response = requests.get(url)
        data = response.json()

        output['from'] = currency_from.upper()
        output['to'] = currency_to.upper()
        output['exchange_rate'] = data['info']['rate']
        output['date'] = data['date']
        output['from_value'] = round(currency_from_value, 2)
        output['to_value'] = round(currency_from_value * output['exchange_rate'], 2) 

        # if currency to or from is AUD or JPY 
        if output['to'] == 'AUD':
            output['to_value'] = round05(output['to_value'])
        if output['to'] == 'JPY':
            output['to_value'] = round(math.floor(output['to_value']))

        if output['from'] == 'AUD':
            output['from_value'] = round05(output['from_value'])
        if output['from'] == 'JPY':
            output['from_value'] = round(math.floor(output['from_value']))


# round to nearest 5 cents 
# for AUD (EUR)* currency  
def round05(n):
    return round(n * 2) / 2

    
