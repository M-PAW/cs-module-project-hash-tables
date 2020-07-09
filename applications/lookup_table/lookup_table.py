# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# create a cache
slowfun_cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    # define value of v
    v = math.pow(x, y)
    
    # check if is already in cache
    if v in slowfun_cache:
        v = slowfun_cache[v]

    # else perform calcs
    else:
        slowfun_cache[v] = math.factorial(v)
        slowfun_cache[v] //= (x + y)
        slowfun_cache[v] %= 982451653
        # utilize recursion goodness with a reassignment
        v = slowfun_cache[v]
    # return v
    return v




# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
