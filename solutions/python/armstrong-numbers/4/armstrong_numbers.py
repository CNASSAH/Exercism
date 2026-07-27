import math
""" 
Module providing math formulas
"""

def is_armstrong_number(number):
    """ function that guess if a number is an Armstrong number
    ex : 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
         154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    """
    if number == 0:
        number_of_digits = 1
    else:
        number_of_digits = math.floor(math.log(number, 10)) + 1
        
    temp = number
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** number_of_digits
        temp //= 10

    return total_sum == number
