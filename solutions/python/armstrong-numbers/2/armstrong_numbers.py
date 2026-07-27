import math

def is_armstrong_number(number):
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


