import math

def abs_sign(v1):
    if v1 > 0:
        return v1
    elif v1 <= 0:
        return -v1

def abs_square(v1):
    a = v1 * v1
    return math.isqrt(a) # return result as float

print(abs_sign(-3))
print(abs_square(5))
