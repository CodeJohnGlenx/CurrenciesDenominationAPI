"""
test.py 

- test the functionality of regex.py 
- test the correctness and accuracy of regex.py
"""

import regex
import random 
import time
from typing import Union

# generate random seed
random.seed(int(time.time()))

# type of currency 
currency = regex.JPY
curr = "JPY"

# denomination_output: dict - return value of regex.get_denomination()
# expected_sum: int | float - expected answer of denomination_output when all denominations are added back
def test_regex_py(denomination_output: dict, expected_sum: Union[int, float]):
    denomination_sum = 0
    
    # add denomination values
    for d in denomination_output:
        denomination_sum += round(int(denomination_output[d]) * float(str(d)), 2)

    if (denomination_sum == int(denomination_sum)):
        denomination_sum = int(denomination_sum)

    # print result 
    print(f"deno sum: {round(denomination_sum, 2)} | exp sum: {expected_sum} | result: {round(denomination_sum, 2)==expected_sum}")

    # return result
    return round(denomination_sum, 2) == expected_sum


# conduct testing 
correct = 0
number_test = random.randint(1, 10000)  # number of test

for i in range(0, number_test):
    is_float = random.randint(0, 1) # if test number is float
    float_part = 0
    test_num = 0

    # add floating-point number 
    if is_float == 1:
        #float_part = random.randint(0, 99) / 100
        pass
    
    # whole number + (floating-point number)*
    test_num = round(random.randint(0, 1000000) + float_part, 2)
    
    # increment correct for every correct test
    correct += 1 if test_regex_py(regex.get_denomination(currency, test_num), test_num) == 1 else 0

print()
print(f"type of currency: {curr}")
print(f'correct result: {correct}/{number_test}')

"""
TO DO:
# add documentation comment
"""
    

