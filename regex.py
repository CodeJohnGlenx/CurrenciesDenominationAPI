"""
regex.py

- specifies the regex of each currency (PHP, USD, EUR, JPY, AUD)
- gets the denomination of a currency 
"""

import re 
from typing import Union
import ast

# Philippine Peso (PHP) Denomination Regex
PHP = {
    '1000': '^[1-9]\d{3,}(.\d{1,2})?$',  # 1000 and above
    '500': '^[5-9]\d{2,}(.\d{1,2})?$',  # 500-999.99
    '200': '^[2-4]\d{2,}(.\d{1,2})?$',  # 200-499.99
    '100': '^1\d{2,}(.\d{1,2})?$',   # 100-199.99
    '50': '^[5-9]\d(.\d{1,2})?$',  # 50-99.99
    '20': '^[2-4]\d(.\d{1,2})?$',  # 20-49.99
    '10': '^1\d(.\d{1,2})?$',  # 10-19.99
    '5': '^[5-9](.\d{1,2})?$',  # 5-9.99
    '1': '^[1-4](.\d{1,2})?$',  # 1-4.99
    '0.25': '^0.2[5-9]$|^0.[3-9](\d)?$',  # 0.25-0.99
    '0.1': '^0.1(\d)?$|^0.2([0-4])?$',  # 0.10-0.24
    '0.05': '^0.0[5-9]$',  # 0.05-0.09
    '0.01': '^0.0[1-4]$',  # 0.01-0.04
}

# United States Dollars (USD) Denomination Regex
USD = {
    '100': '^[1-9]\d{2,}(.\d{1,2})?$', # 100 and above
    '50': '^[5-9]\d(.\d{1,2})?$',  # 50-99.99
    '20': '^[2-4]\d(.\d{1,2})?$',  # 20-49.99
    '10': '^1\d(.\d{1,2})?$',  # 10-19.99
    '5': '^[5-9](.\d{1,2})?$',  # 5-9.99
    '2': '^[2-4](.\d{1,2})?$', # 2-4.99
    '1': '^1(.\d{1,2})?$',  # 1-1.99
    '0.5': '^0.[5-9](\d)?$', # 0.5-0.99
    '0.25': '^0.2[5-9]$|^0.[3-4](\d)?$',  # 0.25-0.49
    '0.1': '^0.1(\d)?$|^0.2([0-4])?$',  # 0.10-0.24
    '0.05': '^0.0[5-9]$',  # 0.05-0.09
    '0.01': '^0.0[1-4]$',  # 0.01-0.04
}

# Euro (EUR) Denomination Regex
EUR = {
    '500': '^([5-9]\d{2,}|[1-9]\d{3,})(.\d{1,2})?$', # 500 and above
    '200': '^[2-4]\d{2,}(.\d{1,2})?$',  # 200-499.99
    '100': '^1\d{2,}(.\d{1,2})?$',   # 100-199.99
    '50': '^[5-9]\d(.\d{1,2})?$',  # 50-99.99
    '20': '^[2-4]\d(.\d{1,2})?$',  # 20-49.99
    '10': '^1\d(.\d{1,2})?$',  # 10-19.99
    '5': '^[5-9](.\d{1,2})?$',  # 5-9.99
    '2': '^[2-4](.\d{1,2})?$', # 2-4.99
    '1': '^1(.\d{1,2})?$',  # 1-1.99
    '0.5': '^0.[5-9](\d)?$', # 0.5-0.99
    '0.2': '^0.[2-4](\d)?$',  # 0.2-0.49
    '0.1': '^0.1(\d)?$',  # 0.10-0.19
    '0.05': '^0.0[5-9]$',  # 0.05-0.09
    '0.02': '^0.0[2-4]$', # 0.02-0.04
    '0.01': '^0.01$', # 0.01
}


# Australian Dollars (AUD) Denomination Regex
# note: AUD 1 cents and 2 cents are no longer used
# round to nearest 5 cents 0: [0, 1, 2]
AUD = {
    '100': '^[1-9]\d{2,}(.\d{1,2})?$', # 100 and above
    '50': '^[5-9]\d(.\d{1,2})?$',  # 50-99.99
    '20': '^[2-4]\d(.\d{1,2})?$',  # 20-49.99
    '10': '^1\d(.\d{1,2})?$',  # 10-19.99
    '5': '^[5-9](.\d{1,2})?$',  # 5-9.99
    '2': '^[2-4](.\d{1,2})?$', # 2-4.99
    '1': '^1(.\d{1,2})?$',  # 1-1.99
    '0.5': '^0.[5-9](\d)?$', # 0.5-0.99
    '0.2': '^0.[2-4](\d)?$',  # 0.2-0.49
    '0.1': '^0.1(\d)?$',  # 0.10-0.19
    '0.05': '^0.0[5-9]$',  # 0.05-0.09
}

# Japanese Yen (JPY) Denomination Regex
# JPY has no cents and the lowest denomination is 1 yen 
# excess cents are truncated
JPY = {
    '10000': '^[1-9]\d{4,}(.\d{1,2})?$', # 10000 and above
    '5000': '^[5-9]\d{3,}(.\d{1,2})?$', # 5000-9999
    '2000': '^[2-4]\d{3,}(.\d{1,2})?$', # 2000-4999
    '1000': '^1\d{3,}(.\d{1,2})?$', # 1000-1999
    '500': '^[5-9]\d{2,}(.\d{1,2})?$',  # 500-999
    '100': '^[1-4]\d{2,}(.\d{1,2})?$',   # 100-499
    '50': '^[5-9]\d(.\d{1,2})?$',  # 50-99
    '10': '^[1-4]\d(.\d{1,2})?$',  # 10-49
    '5': '^[5-9](.\d{1,2})?$',  # 5-9
    '1': '^[1-4](.\d{1,2})?$',  # 1-4
}

currencies = {
    'PHP': PHP,
    'USD': USD,
    'EUR': EUR,
    'AUD': AUD,
    'JPY': JPY,
}

"""
get_denomination(denomination: dict, value: float) - converts a currency value into a denomination with respect to the provided type of currency 

parameters:
# denomination: dict - a dictionary of strings that will be passed in a regex matching 
# value: float - a float value that will be broken down into denomination 

returns -> dict - a dictionary containing denomination values
"""
def get_denomination(denomination: dict, value: Union[int, float], available_denomination: str):
    denomination_output = {}

    if available_denomination != "all":
        available_denomination = ast.literal_eval(available_denomination)
        available_denomination.sort(reverse=True)
        available_denomination = list(dict.fromkeys(available_denomination))
        available_denomination = [str(i) for i in available_denomination]

    if available_denomination == "all":
        # iterate every denomination regex rule 
        for d in denomination:
            # get number of denomination if regex matches 
            if re.match(denomination[d], str(value)):
                print(available_denomination)
                # whole number processing
                if value >= 1:
                    denomination_output[d] = int(value // int(d))
                    value = round(value % int(d), 2)
                # floating-part processing
                else:
                    denomination_output[d] = int(round(value / float(d), 3))
                    value = round(value % float(d), 2)
    else:
        for d in denomination:
            if d in available_denomination:
                if value >= 1:
                    denomination_output[d] = int(value // float(d))
                    value = round(value % float(d), 2)
                # floating-part processing
                else:
                    denomination_output[d] = int(round(value / float(d), 3))
                    value = round(value % float(d), 2)
    
    return denomination_output


"""
print(get_denomination(PHP, 50))
print(get_denomination(EUR, 1827.73))
print(get_denomination(USD, 100.1))
print(get_denomination(AUD, 3745.76))
print(get_denomination(JPY, 433451.76))
"""




