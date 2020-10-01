import sys
#-------------------------------------
name_list = ["keroro","kiroro1","dororo","tamama","kiroro2","kururu"]
#-------------------------------------
def Paring_two_friends(array_values):
    # print("in it? 1")
    name_set = set()
    length = len(array_values)
    print("Total "+length.__str__()+" Friends")
    print("------Paring Two Friends - For--------")
    global count # 전역변수 선언 방법
    count = 0 # 전역변수 선언 방법
    for i in range(0, length-1):
        for j in range(i+1, length):
            print(array_values[i]+" - "+array_values[j])
            count += 1
        print("-------FOR 1--------")


print("------Paring Two Friends - For--------")
Paring_two_friends(name_list)
print(count, end =" = ")
# print("Same name set", end =" ")
print(len(name_list)*(len(name_list)-1)//2) # n(n-1)/2 Combination
#-------------------------------------

# # # Result
# ------Paring Two Friends - For--------
# Total 6 Friends
# ------Paring Two Friends - For--------
# keroro - kiroro1
# keroro - dororo
# keroro - tamama
# keroro - kiroro2
# keroro - kururu
# -------FOR 1--------
# kiroro1 - dororo
# kiroro1 - tamama
# kiroro1 - kiroro2
# kiroro1 - kururu
# -------FOR 1--------
# dororo - tamama
# dororo - kiroro2
# dororo - kururu
# -------FOR 1--------
# tamama - kiroro2
# tamama - kururu
# -------FOR 1--------
# kiroro2 - kururu
# -------FOR 1--------
# 15 = 15
