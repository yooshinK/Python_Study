import math
#-------------------------------------
def find_GCF(v1,v2):
    if v1 == v2:
        return v1

    elif v1 < v2:
        s = v1
        while s >= 1:
            if (v2 % s) == 0:
                return s
            else:
                s -= 1
    else:
        s = v2
        while s >= 1:
            if (v1 % s) == 0:
                return s
            else:
                s -= 1
#-------------------------------------
num1 = int(input("Enter the first num - "))
num2 = int(input("Enter the second num - "))

print("The Greatest Common Factor is", end =" ")
print(find_GCF(num1, num2))
#-------------------------------------
# # Resutl
