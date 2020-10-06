import math
#-------------------------------------
def Euclidean_algorithm(v1,v2):
    min_idx = min(v1,v2)
    max_idx = max(v1,v2)
    if min_idx == 0:
        return max_idx
    elif min_idx != 0:
        return Euclidean_algorithm(min_idx ,max_idx % min_idx)
#-------------------------------------
def Euclidean_algorithm(a,b):
    if b == 0:
        return a
    return Euclidean_algorithm(b, (a % b))
#-------------------------------------
num1 = int(input("Enter the first num - "))
num2 = int(input("Enter the second num - "))

print("The Greatest Common Factor - Euclidean Algorithm", end =" - ")
print(Euclidean_algorithm(num1, num2))
#-------------------------------------
