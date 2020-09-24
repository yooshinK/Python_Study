import math
#-------------------------------------
def sum_factorial(n):
    if n > 0:
        return n+sum_factorial(n-1)
    elif n < 0:
        return n+sum_factorial(n+1)
    else:
        return 0
#-------------------------------------
def sum_for(n):
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s = s + i
    elif n < 0:
        for i in range(n,1):
            s = s + i
    else:
        return 0
    return s
#-------------------------------------

print("------sum factorial--------")
print("Sum = "+sum_factorial(10).__str__())
print("Sum = "+sum_factorial(-10).__str__())

print("------sum for--------")
print("Sum = "+sum_for(10).__str__())
print("Sum = "+sum_for(-10).__str__())

print("Factorial value is "+math.factorial(5).__str__())
# # Resutl
# Sum value is 5050
# Sum value is -5050
# Factorial value is 120
