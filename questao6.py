from math import floor, sqrt

def is_prime(n):
    if n <= 1:
        return False

    for k in range(2, floor(sqrt(n))+1):
        if n % k == 0:
            return False
        
    return True

assert(is_prime(2))
assert(is_prime(3))
assert(is_prime(5))
assert(is_prime(11))
assert(not is_prime(35))
assert(is_prime(19911121))
assert(not is_prime(19980612))