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
def Fibonacci_Sequence_recursive1(v1,v2,index):
    print("Fibonacci Sequence - Resucrtive 1st - ", v1, v2, index)
    v3 = v1+v2
    while index > 2:
        index -= 1
        return Fibonacci_Sequence_recursive1(v2, v3, index)
    return v3
#-------------------------------------
# num = int(input("Enter a number - "))
num = 3
print("Fibonacci Sequence For ", num)
print(Fibonacci_Sequence_for(num))
print("Fibonacci Sequence Recursive 1st - ", num)
print(Fibonacci_Sequence_recursive1(0,1,num))
#-------------------------------------
# Result:
