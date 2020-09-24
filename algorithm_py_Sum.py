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
def sum_Gauss(n):
    s = 0
    if n > 0:
        s = n*(n+1)/2
    elif n < 0:
        s = (n*(n-1)/2)*-1
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

print("------sum Gauss--------")
print("Sum = "+sum_Gauss(10).__str__())
print("Sum = "+sum_Gauss(-10).__str__())

print("------Just Factorial--------")
print("Factorial value is "+math.factorial(5).__str__())

# # Resutl
# ------sum factorial--------
# Sum = 55
# Sum = -55
# ------sum for--------
# Sum = 55
# Sum = -55
# ------sum Gauss--------
# Sum = 55.0
# Sum = -55.0
# ------Just Factorial--------
# Factorial value is 120
