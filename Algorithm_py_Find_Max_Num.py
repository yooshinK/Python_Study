import math
#-------------------------------------
num_list = [17,902,18,33,58,700,330,4550]
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
    return s, max_idx
#-------------------------------------
def find_max_num_recursive(array_values, n):
    if n > 0:
        Max_num = find_max_num_recursive(array_values, n-1)
        if array_values[n] <= Max_num:
            return Max_num
        else:
            return array_values[n]
    elif n == 0:
        return array_values[0]

#-------------------------------------

print("------Find Max Num - For--------")
print(find_max_num_for(num_list))
print("------Find Max Num - Recursive--------")
print(find_max_num_recursive(num_list, len(num_list)-1))
#-------------------------------------

# # Result
# ------Find Max Num - For--------
# Max Id is 1
# (902, 1)
# ------Find Max Num - Recursive--------
# 902
