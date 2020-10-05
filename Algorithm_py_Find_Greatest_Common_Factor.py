import math
#-------------------------------------
def find_GCF(v1,v2):
    if v1 == v2:
        return v1
        
    elif v1 < v2:
        i = v1
        for i in range(i, 1):
            if (v2 / i) == 0:
                return i
            else:
                i -= 1
    else:
        i = v2
        for i in range(i, 1):
            if (v1 / i) == 0:
                return i
            else:
                i -= 1
#-------------------------------------
num1 = int(input("Enter the first num"))
num2 = int(input("Enter the second num"))

print('The Greatest Common Factor is')
find_GCF(num1, num2)
#-------------------------------------
# # Resutl
