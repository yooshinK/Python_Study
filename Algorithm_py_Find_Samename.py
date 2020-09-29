import math
#-------------------------------------
num_list = [17,92,18,33,58,70,330,420]
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
        # else:
        #     pass

print("------Find Max Num - For--------")
print(find_max_num_for(num_list))
#-------------------------------------

# # Result
# ------Find Max Num - For--------
# Max Id is 7
# (420, 7)
