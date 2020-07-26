#function basic format
def a3():
    print('aaa')
    pass

for i in range(3): # i = 0
    a3()
    i += 1

print("-----------------------------")
#function return

def b3():
    print("Python b3's return")
    return 'Python bbb'

print(b3())
