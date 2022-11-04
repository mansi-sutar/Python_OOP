# 1
class Dept:
    dept = "CST"
    def print(self):
        print("Name :", self.name)
        print("Roll no. :", self.roll_no)
        print("Dept. :", self.dept)
        print("")

class Stud1(Dept):
    def func1(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


class Stud2(Dept):
    def func2(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

D = Dept()
S1 = Stud1()
S1.func1('Mansi',36)
S2 = Stud2()
S2.func2('Riya',24)

S1.print()
S2.print()





# 2
class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


c1 = Child1()
c2 = Child2()
c1.func1()
c1.func2()
c2.func1()
c2.func3()
