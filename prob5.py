#2520 is the smallest number that can be divided by each of the numbers from 1
#to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

def factorize(num, final_dict):
    '''
    Factorizes a number in its prime factors and if one of those factors is
    repeated more times than we've already seen in previous number, switches
    the values.
    '''
    primes_list = []
    i = 2
    while num != 1:
        j = 0
        while num % i == 0:
            num /= i
            j += 1
        if j > 0:
            if i not in final_dict or j > final_dict[i]:
                final_dict[i] = j
        i += 1

def find_lowest_divisible(num):
    '''
    (int) -> int
    Returns lowest possible number that is evenly divisible by all numbers
    in a given range
    '''
    final_dict = {}
    for i in range(1,num + 1):
        factorize(i, final_dict)
    total = 1
    for key in final_dict:
        total *= key ** final_dict[key]
    return total



print find_lowest_divisible(20)
