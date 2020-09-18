class Class_TEST1():
    def C_T1_method(arg):
        print("This is Class_TEST1's Method")

class Class_TEST2():
    def C_T2_method(arg):
        print("This is Class_TEST2's Method")

class Class_TEST3(Class_TEST1,Class_TEST2): #다중상속
    pass # 이 클래스, 함수는 기능이 없다는 뜻으로 항상 적어주어야한다.

c = Class_TEST3()
c.C_T1_method()
c.C_T2_method()
