import sys
#-------------------------------------
name_list = ["keroro","kiroro","dororo","tamama","kiroro","kururu","kururu","kururu","dororo","tamama"]
#-------------------------------------
def find_Samename(array_values):
    # print("in it? 1")
    name_set = set()
    length = len(array_values)
    print(length)
    global count # 전역변수 선언 방법
    count = 0 # 전역변수 선언 방법
    for i in range(0, length-1):
        s = array_values[i]
        print("FOR 1 in it / i is - "+ i.__str__() + ", " + s.__str__())
        for j in range(i+1, length):
            print("FOR 2 in it / j is - "+ j.__str__())
            if s == array_values[j]:
                print("in it? IF ")
                count += 1
                print(s, count)
                name_set.add(s)
                s = array_values[i]
        print("-------FOR 1--------")
    # print("Max Id is " + max_idx.__str__())
    return name_set
        # else:
        #     pass

print("------Find Same Name - For--------")
print("Same name set", end =" ") # on the same line printing
# sys.stdout.write("TEST") # on the same line printing
print(find_Samename(name_list))
print(count)
#-------------------------------------

# # # Result
# ------Find Same Name - For--------
# Same name set 10
# FOR 1 in it / i is - 0, keroro
# FOR 2 in it / j is - 1
# FOR 2 in it / j is - 2
# FOR 2 in it / j is - 3
# FOR 2 in it / j is - 4
# FOR 2 in it / j is - 5
# FOR 2 in it / j is - 6
# FOR 2 in it / j is - 7
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 1, kiroro
# FOR 2 in it / j is - 2
# FOR 2 in it / j is - 3
# FOR 2 in it / j is - 4
# in it? IF
# kiroro 1
# FOR 2 in it / j is - 5
# FOR 2 in it / j is - 6
# FOR 2 in it / j is - 7
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 2, dororo
# FOR 2 in it / j is - 3
# FOR 2 in it / j is - 4
# FOR 2 in it / j is - 5
# FOR 2 in it / j is - 6
# FOR 2 in it / j is - 7
# FOR 2 in it / j is - 8
# in it? IF
# dororo 2
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 3, tamama
# FOR 2 in it / j is - 4
# FOR 2 in it / j is - 5
# FOR 2 in it / j is - 6
# FOR 2 in it / j is - 7
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# in it? IF
# tamama 3
# -------FOR 1--------
# FOR 1 in it / i is - 4, kiroro
# FOR 2 in it / j is - 5
# FOR 2 in it / j is - 6
# FOR 2 in it / j is - 7
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 5, kururu
# FOR 2 in it / j is - 6
# in it? IF
# kururu 4
# FOR 2 in it / j is - 7
# in it? IF
# kururu 5
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 6, kururu
# FOR 2 in it / j is - 7
# in it? IF
# kururu 6
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 7, kururu
# FOR 2 in it / j is - 8
# FOR 2 in it / j is - 9
# -------FOR 1--------
# FOR 1 in it / i is - 8, dororo
# FOR 2 in it / j is - 9
# -------FOR 1--------
# {'dororo', 'kururu', 'tamama', 'kiroro'}
# 6
