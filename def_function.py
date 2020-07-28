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

print("-----------------------------")
#function Input X 1

def c(num):
    print("Python Function C's input")
    print(num)
    return num*'c'
print(c(100))

print("-----------------------------")
#function Input X 2

def alphabet(num,str):
    print("Python Function Alphabet")
    print(num)
    print(str)
    return num*str

print(alphabet(100,'K'))
