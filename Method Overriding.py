# 1
class Dept:
    dept = "CST"

class Stud1(Dept):
    def func(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("Name :", self.name)
        print("Roll no. :", self.roll_no)
        print("Dept. :", self.dept)
        print("")

class Stud2(Dept):
    def func(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("Name :", self.name)
        print("Roll no. :", self.roll_no)
        print("Dept. :", self.dept)
        print("")

S1 = Stud1()
S2 = Stud2()
S1.func('Mansi',36)
S2.func('Riya',24)
S1.display()
S2.display()

# 2
class base:
    def show1(self):
        print("This is base cls.")

class derived(base):
    def show(self):
        print("This is derived cls.")

d = derived()
d.show()
