import random
import math

lookup_table = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    
    # Create a 2-tuple to use as a key into a loookup table
    my_pair = (x, y)

    # if an entry for the pair exists, retrieve the value
    if my_pair in lookup_table:
        return lookup_table[my_pair]

    # else calculate the answer
    answer_for_pair = slowfun_too_slow(x, y)

    # and store the answer in the lookup table
    lookup_table[my_pair] = answer_for_pair

    # and return the answer
    return answer_for_pair







# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
