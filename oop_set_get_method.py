class Cal(object):
    def __init__(self, v1, v2): #생성자, Constructor -> 자동호출
        print(v1,v2) #a and b are local variables
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1+self.v2 # self. are instance variables. could be other letters
    def subtract(self):
        return self.v1-self.v2
    def setV1(self,v):
        if isinstance(v, int):
            self.v1 = v
        elif isinstance(v, str):
            print("Please input integer only")
    def getV1(self):
        return self.v1

c1 = Cal(10,7)
print(c1.add())
print(c1.subtract())
c1.setV1('Seven')
print(c1.setV1(1235111)) # Result: None
print(c1.v1) # Result: 1235111
print(c1.getV1()) # Result: 1235111

c2 = Cal(30,3)
print(c2.add())
print(c2.subtract())
