import math
#-------------------------------------
def find_LCM(v1,v2):
    if v1 != 0 and v2 != 0:
        return (v1*v2) // find_CGF(v1,v2)
    else:
        return 0
#-------------------------------------
def find_CGF(v1,v2):
    s = min(v1,v2)
    while True:
        if (v1 % s) == 0 and (v2 % s) == 0 :
            return s
        else:
            s -= 1
#-------------------------------------
# num1 = int(input("Enter the first num - "))
# num2 = int(input("Enter the second num - "))

print("The Least Common Multiple Factor - Function", end =" : ")
print(find_LCM(72, 192))
#-------------------------------------
# # Result
# The Least Common Multiple Factor - Function 576
