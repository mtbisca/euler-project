def sum_up_to(value):
    '''
    (int) -> int
    Return sum of all numbers up to a certain value.
    >>> sum_up_to(1)
    1
    >>> sum_up_to(3)
    6
    >>> sum_up_to(0)
    0
    '''

    return int((1 + value) * (value / 2.0))

def sum_of_squares(value):
    '''
    (int) -> int
    Return sum of the squares of all numbers up to a certain value.
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(2)
    5
    >>> sum_of_squares(3)
    14
    '''
    return sum([n ** 2 for n in range(value + 1)])

def difference(value):
    '''
    (int) -> int
    Return absolute difference between the square of the sum of all numbers
    up to a certain value and the sum of all squares up to that same value.
    >>> difference(1)
    0
    >>> difference(3)
    22
    '''
    return abs(sum_of_squares(value) - sum_up_to(value)**2)

print difference(100)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
