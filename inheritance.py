class Class1(object):
    # def __init__(self, arg):
    #     super(Class1 self).__init__()
    #     self.arg = arg
    def method1(self):
        return 'Inheritance Test Class1 Method1'

c1 = Class1()
print(c1, c1.method1())

class Class2(object):
    def method1(self): return 'Inheritance Test Class2 Method1'
    def method2(self): return 'Inheritance Test Class2 Method2'

c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())

print("---------------------------------")

class Class3(Class1): #Python's Inheritance Parent:Class1
    def method2(self): return 'Inheritance Test Class3 Method2'
    # def method1(self): return 'Inheritance Test Class3 Method1' -> can be updated 

c3 = Class3()
print(c3, c3.method1())
print(c3, c3.method2())

# Result
# <__main__.Class1 object at 0x000001F0502A84F0> Inheritance Test Class1 Method1
# <__main__.Class2 object at 0x000001F0502A8C70> Inheritance Test Class2 Method1
# <__main__.Class2 object at 0x000001F0502A8C70> Inheritance Test Class2 Method2
# ---------------------------------
# <__main__.Class3 object at 0x000001F0502D9A30> Inheritance Test Class1 Method1
# <__main__.Class3 object at 0x000001F0502D9A30> Inheritance Test Class3 Method2
