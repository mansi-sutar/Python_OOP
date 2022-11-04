# 1
class Parent:
    def f1(self):
        print("Parent class function called...!!!")

class Child(Parent):
    def f2(self):
        print("Child class function called...!!!")

c = Child()
c.f1()
c.f2()
