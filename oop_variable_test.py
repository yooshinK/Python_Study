class Test_Class:
    def __init__(self, arg):
        self.test_value = arg
    def show(self):
        print(self.test_value)

c1 = Test_Class(10)

# Python allows users to access instance variables directly.
print(c1.test_value)
c1.test_value = 20
print(c1.test_value)

# Users can also see the variables' values via
c1.show()
