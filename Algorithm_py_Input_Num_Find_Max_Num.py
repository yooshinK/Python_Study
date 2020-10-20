import math
#-------------------------------------
def find_max_num_for(array_values):
    n = len(array_values)
    s = array_values[0]
    max_idx = 0
    for i in range(1, n):
        if s <= array_values[i]:
            s = array_values[i]
            max_idx = i
    print("Max Id is " + max_idx.__str__())
    print("Max Number is ", s)
#-------------------------------------
num_list = []
num = int(input("Enter how many elements you want"))
print('Enter numbers in array: ')
for i in range(0,num):
    # a = int(input("num :"))
    num_list.append(int(input("num :")))
find_max_num_for(num_list)
print('ARRAY: ', num_list)
#-------------------------------------
# # Result
