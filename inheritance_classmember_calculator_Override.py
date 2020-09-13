class Cal(object):
    _Cal_history = []
    def __init__(self, v1, v2): #생성자, Constructor -> 자동호출
        print("-------Initialize------") #a and b are local variables
        if isinstance(v1,int):
            self.v1 = v1
        if isinstance(v2,int):
            self.v2 = v2

    def setV1(self,v):
        if isinstance(v, int):
            self.v1 = v
        elif isinstance(v, str):
            print("Please input integer only")

    def getV1(self):
        return self.v1

    def add(self):
        result = self.v1+self.v2 # self. are instance variables. could be other letters
        Cal._Cal_history.append("add : %d + %d = %d" % (self.v1,self.v2,result))
        return result
    def subtract(self):
        result = self.v1-self.v2 # self. are instance variables. could be other letters
        Cal._Cal_history.append("subtract : %d - %d = %d" % (self.v1,self.v2,result))
        return result
    @classmethod
    def Cal_history(cls):
        for word in Cal._Cal_history: # print array with new line
            print(word)
        print("\n".join(Cal._Cal_history)) # print array with new line
    def info(self):
        return "Information Cal -> v1 : %d, v2 : %d" % (self.v1, self.v2)
#-------------------------------------------------------------
class CalMutiply(Cal): #Python's Inheritance Parent:Cal
    def multiply(self):
        result = self.v1*self.v2 # self. are instance variables. could be other letters
        Cal._Cal_history.append("multiply : %d X %d = %d" % (self.v1,self.v2,result))
        return result
    def info(self):
        return "Information CalMultiply => %s" % super().info()
#-------------------------------------------------------------
class CalDivide(CalMutiply): #Python's Inheritance Parent:Cal
    def divide(self):
        result = self.v1/self.v2 # self. are instance variables. could be other letters
        Cal._Cal_history.append("divide : %d / %d = %d" % (self.v1,self.v2,result))
        return result
    def info(self):
        return "Information Devide => %s" % super().info()
#-------------------------------------------------------------

c0 = Cal(111,333)
print(c0.add())
print(c0.subtract())
print(c0.info())

print("--------------------------------")

c1 = CalMutiply(8,6)
print(c1.add())
print(c1.subtract())
print(c1.multiply())
print(c1.info())


print("--------------------------------")

c2 = CalDivide(18,9)
print(c2.add())
print(c2.subtract())
print(c2.multiply())
print(c2.divide())
print(c2.info())

print("--------------------------------")
c2.Cal_history()
