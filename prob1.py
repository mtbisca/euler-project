##If we list all the natural numbers below 10 that are multiples of 3 or 5,
##we get 3, 5, 6 and 9. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000.

def find_sum(max_range):
    '''
    (int) -> int
    Returns sum of all multiples of 3 and 5 up to a given range.
    >>> find_sum(10)
    23
    '''
    return sum([n for n in range(max_range) if not(n % 3) or not(n % 5)])

if __name__ == '__main__':
    print find_sum(1000)
