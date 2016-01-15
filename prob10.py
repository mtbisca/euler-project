import math
primes_list = [2]

def is_prime(num):
    '''
    (int) -> bool

    Test if given number is a prime number.

    >>> is_prime(7)
    True
    >>> is_prime(5)
    True
    >>> is_prime(8)
    False
    '''
    num_root = math.sqrt(num)
    for prime in primes_list:
        if num % prime == 0 and num != prime:
            return False
        if prime >= num_root:
            break
    primes_list.append(num)
    return True

def find_prime_sum_below(n):
    '''
    (int) -> int

    Find sum of all prime numbers below a given number.

    >>> find_prime_sum_below(10)
    17
    >>> find_prime_sum_below(5)
    5
    >>> find_prime_sum_below(7)
    10
    '''
    prime_sum = 2
    for i in range(3, n):
        if is_prime(i):
            prime_sum += i
    return prime_sum

print find_prime_sum_below(2000000)
