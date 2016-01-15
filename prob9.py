def is_pythagorean_triplet(a, b, c):
    '''
    (int, int, int) -> bool

    Test if three given values compose a Pythagorean triplet.

    >>> is_pythagorean_triplet(3,4,5)
    True
    >>> is_pythagorean_triplet(4,5,3)
    True
    >>> is_pythagorean_triplet(5,3,4)
    True
    >>> is_pythagorean_triplet(3,5,6)
    False

    '''
    return (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or
    b**2 + c**2 == a**2)


def finds_pythagorean_product():
    '''
    () -> int

    Return product of Pythagorean triplet that adds up to 1000.
    '''
    for a in range(1,1001):
        b = a + 1
        while b < 1000 - a:
            c = 1000 - a - b
            if c >= 0 and is_pythagorean_triplet(a,b,c):
                return a * b * c
            else:
                b += 1
print finds_pythagorean_product()
