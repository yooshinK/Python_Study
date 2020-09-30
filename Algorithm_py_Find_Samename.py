import sys
#-------------------------------------
name_list = ["keroro","kiroro","dororo","tamama","kiroro","kururu","dororo"]
#-------------------------------------
def find_Samename(array_values):
    # print("in it? 1")
    name_set = set()
    length = len(array_values)
    count = 0
    for i in range(0, length-2):
        # print("FOR 1 in it?")
        s = array_values[i]
        for j in range(i+1, length-1):
            # print("FOR 2 in it?")
            if s == array_values[j]:
                name_set.add(s)
                s = array_values[i]
                count += 1
                # print("in it? IF ")

    # print("Max Id is " + max_idx.__str__())
    return name_set
        # else:
        #     pass

print("------Find Same Name - For--------")
print("Same name set", end =" ") # on the same line printing
# sys.stdout.write("TEST") # on the same line printing
print(find_Samename(name_list))
#-------------------------------------

# # Result
