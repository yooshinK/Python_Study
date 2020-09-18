class Class_TEST1():
    def C_T1_method(arg):
        print("This is Class_TEST1's Method")
    def basic_method(self):
        print("Basic Method of Class_TEST1")

class Class_TEST2():
    def C_T2_method(arg):
        print("This is Class_TEST2's Method")
    def basic_method(self):
        print("Basic Method of Class_TEST2")

class Class_TEST3(Class_TEST1,Class_TEST2): #다중상속
    def basic_method(self):
        print("Basic Method of Class_TEST3")
    pass # 이 클래스, 함수는 기능이 없다는 뜻으로 항상 적어주어야한다.

c = Class_TEST3()
c.C_T1_method()
c.C_T2_method()
c.basic_method()

# 호출 우선순위 보기 .__mro__
#(<class '__main__.Class_TEST3'>, <class '__main__.Class_TEST1'>, <class '__main__.Class_TEST2'>, <class 'object'>)
print(Class_TEST3.__mro__)
#basic_method TEST3이 없으면 첫번째의 부모클래스의 동일한 함수를 불러온다.
