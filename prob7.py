def find_nth_prime(n):
    '''
    (int) -> int

    Find the nth prime number.

    >>>find_nth_prime(1)
    2
    >>>find_nth_prime(3)
    5
    >>>find_nth_prime(6)
    13
    '''
    primes_list = [2]
    i = 3
    while len(primes_list) <= n:
        is_prime = True
        for number in primes_list:
            if i % number == 0:
                is_prime = False
        if is_prime:
            primes_list.append(i)
        i += 1
    return primes_list[n - 1]

print find_nth_prime(10001)
