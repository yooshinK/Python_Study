class Class_Variable_Test(object):
    count = 0  # 해당 클래스의 인스턴스가 모두 공유하는 변수
    def __init__(self):
        Class_Variable_Test.count += 1 # When you access class variables in a method
    @classmethod
    def getCount(cls):
        print(cls) #
        return cls.count

i1 = Class_Variable_Test()
i2 = Class_Variable_Test()
i3 = Class_Variable_Test()
i4 = Class_Variable_Test()

print(Class_Variable_Test.getCount())
