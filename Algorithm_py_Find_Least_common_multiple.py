import math
#-------------------------------------
def find_LCM1(v1,v2):
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
def find_LCM2(v1,v2):
    s = min(v1,v2)
    while True:
        if (v1 % s) == 0 and (v2 % s) == 0 :
            return s
        else:
            s -= 1
#-------------------------------------
num1 = int(input("Enter the first num - "))
num2 = int(input("Enter the second num - "))

print("The Least Common Multiple Factor - Function 1", end =" ")
print(find_LCM1(num1, num2))
#-------------------------------------
# # Resutl
