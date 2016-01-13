#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def find_largest_prime_factor(num):
    '''
    (int) -> int
    Return largest prime factor of a given number
    >>> find_largest_prime_factor(13195)
    29
    '''
    i = 2
    while num != 1:
        while num % i == 0:
            num /= i
        i += 1
    return i - 1

print find_largest_prime_factor(600851475143)
