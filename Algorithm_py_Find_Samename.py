import sys
#-------------------------------------
name_list = ["keroro","kiroro","dororo","tamama","kiroro","kururu"]
#-------------------------------------
def find_Samename(array_values):
    name_set = set()
    name_set.add("test")
    length = len(array_values)
    s = array_values[0]
    count = 0
    for i in range(0, length-1):
        if s == array_values[i+1]:
            name_set.add(s)
            count += 1
            print(s)
            s = array_values[i]

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
