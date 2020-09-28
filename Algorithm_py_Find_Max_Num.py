import math
#-------------------------------------
num_list = [17,92,18,33,58,700,33,42]
#-------------------------------------
s = 0
for i in num_list:
    if s <= i:
        s = i
    else:
        pass

print("------Find Max Num - For--------")
print(s)
#-------------------------------------
# # Result
# ------Find Max Num - For--------
# 700

#-------------------------------------
import math
#-------------------------------------
num_list = [17,92,18,33,58,70,330,420]
#-------------------------------------
def find_max_num_for(array_values):
    n = len(array_values)
    s = array_values[0]
    for i in range(1, n):
        if s <= array_values[i]:
            s = array_values[i]
    return s
        # else:
        #     pass

print("------Find Max Num - For--------")
print(find_max_num_for(num_list))
#-------------------------------------

# # Result
# ------Find Max Num - For--------
# 420
