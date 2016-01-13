##Each new term in the Fibonacci sequence is generated
##by adding the previous two terms. By starting with 1 and 2,
##the first 10 terms will be:
##1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
##By considering the terms in the Fibonacci sequence whose values do not
##exceed four million, find the sum of the even-valued terms.

def fibonacci_sum(max_range):
    '''
    (int) -> int
    Returns the sum of all even numbers in a Fibonacci sequence whose values do
    not exceed a given max_range.

    >>>fibonacci_sum(10)
    19
    '''
    prev = 2
    prevprev = 1
    total = 2
    while(prev + prevprev < max_range):
        next_number = prev + prevprev
        if not(next_number % 2):
            total += next_number
        prevprev = prev
        prev = next_number
    return total

if __name__ == '__main__':
    print fibonacci_sum(4000000)
