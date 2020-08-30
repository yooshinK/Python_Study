class Cal(object):
    def __init__(self, value): #생성자, Constructor -> 자동호출
        print("-------Initialize------") #a and b are local variables
        if isinstance(value,int):
            self.v1 = value
            self.__value = value # __value means it does not allow to access or change outside

    def setValue(self,value):
        if isinstance(value, int):
            self.v1 = value
            self.__value = value + 1
        elif isinstance(value, str):
            print("Please input integer only")
    def getValue(self):
        return self.__value

    def show(self):
        print(self.__value)

c1 = Cal(7)
# print(c1.__value) # Result: Error
print(c1.v1) # Result: 1235111

c1.setValue('Seven')
c1.setValue(1235111)

# print(c1.__value) # Result: Error
print(c1.v1) # Result: 1235111

print(c1.getValue()) # Result: 1235112
c1.show() # Result: 1235112
