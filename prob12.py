import math
def get_divisors(num):
    '''
    (int) -> list

    Return list of all divisors of given number.

    >>> get_divisors(8)
    [1, 2, 4, 8]
    >>> get_divisors(3)
    [1, 3]
    >>> get_divisors(1)
    [1]

    '''
    divisor_list = [1]
    num_root = math.sqrt(num)
    for i in range(2, int(math.ceil(num_root))):
        if num % i == 0:
            divisor_list.append(i)
            if num / i not in divisor_list:
                divisor_list.append(num / i)
    if num not in divisor_list:
        divisor_list.append(num)
    return divisor_list

def find_triangular_number(n):
    '''
    (int) -> int
    Return lowest triangular number that has over n divisors

    >>> find_triangular_number(5)
    28
    '''
    i = 1
    current_number = 1
    while len(get_divisors(current_number)) <= n:
        i += 1
        current_number = sum(range(i + 1))

    return current_number

import doctest
doctest.testmod()
print find_triangular_number(500)
