import math

def sum_factorial(n):
    if n > 0:
        return n+sum_factorial(n-1)
    elif n < 0:
        return n+sum_factorial(n+1)
    else:
        return 0

print("Sum value is "+sum_factorial(100).__str__())
print("Sum value is "+sum_factorial(-100).__str__())
print("Factorial value is "+math.factorial(5).__str__())

# # Resutl
# Sum value is 5050
# Sum value is -5050
# Factorial value is 120
