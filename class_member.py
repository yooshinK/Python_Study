class Class_Member_Test:
    @staticmethod
    def static_method():
        print("Static Method")
    @classmethod
    def class_method(cls): # Class method always has to have 'cls'
        print("Class Method")
    def instance_method(self):
        print("Instance Method")

i = Class_Member_Test()
Class_Member_Test.static_method()
Class_Member_Test.class_method()
i.instance_method()
i.static_method() # python works, no errors
i.class_method() # python works, no errors
# Class_Member_Test.instance_method() #Result: Error ! But Python does not allow to use instance method directly without creating instances 
