class Base:
    def fun1(self):
        print("This is Base Class.")

class Derived1(Base):
    def fun2(self):
        print("This is derived class from base class.")

class Derived2(Derived1):
    def fun3(self):
        print("This is also derived class but it is from Derived1 class.")
d = Derived2()
d.fun1()
d.fun2()
d.fun3()