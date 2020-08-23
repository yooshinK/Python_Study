class Cal(object):
    def __init__(self, a, b): #생성자, Constructor -> 자동호출
        print(a,b) #a and b are local variables
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b # self. are instance variables
    def subtract(self):
        return self.a-self.b

c1 = Cal(10,7)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,3)
print(c2.add())
print(c2.subtract())
