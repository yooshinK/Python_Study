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
print(count)

#-------------------------------------

# # # Result
