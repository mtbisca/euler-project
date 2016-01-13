def sum_up_to(value):
    return (1 + value) * (value / 2)
def sum_of_squares(value):
    return sum([n ** 2 for n in range(value + 1)])

def difference(value):
    return abs(sum_of_squares(value) - sum_up_to(value)**2)

print difference(100)
