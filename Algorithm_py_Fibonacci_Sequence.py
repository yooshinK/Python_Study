import math
#-------------------------------------
#-------------------------------------
def Fibonacci_Sequence_for(b):
    print("Fibonacci Sequence FOR - ", end="")
    num_list = [0,1]
    # s = array_values
    for i in range(0, b-2):
        num_list.append(num_list[i]+num_list[i+1])
    return num_list
#-------------------------------------
#-------------------------------------
def Fibonacci_Sequence_recursive(array_values,b):
    print("Fibonacci Sequence - Resucrtive", a, b)
    s = array_values
    if b == 0:
        return 0
    elif b > 0:
        s = s + Fibonacci_Sequence(Fibonacci_Sequence(a,b)*s+1, b-1)
    return s
#-------------------------------------
# num = int(input("Enter a number - "))
num = 11
print("Fibonacci Sequence for ", num)
print(Fibonacci_Sequence_for(num))
#-------------------------------------
# Result:
