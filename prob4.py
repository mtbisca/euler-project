def is_palindrome(s): #3d method-> letter by letter comparisions
    ''' (str) -> bool
    Return True if and only if the given string is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('arara')
    True
    >>> is_palindrome('olar')
    False

    '''
    if(len(s) <= 1):
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

def highest_palindrome_product():
    '''
    () -> int
    Find the highest product between two three-digit numbers that is also
    a palindrome.
    '''
    highest_product = 0
    for i in range(1000):
        for j in range(1000):
            cur_product = i * j
            if is_palindrome(str(cur_product)) and cur_product > highest_product:
                highest_product = i * j
    return highest_product
print highest_palindrome_product()


'''
    One liner solution
def highest_palindrome_product:
    return max([x * y for x in range(1000) for y in range(1000) if str(x * y) == str(x* y)[::-1])
'''
