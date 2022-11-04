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
        self.roll_no = roll_no()

S1 = Stud1()
print(issubclass(Stud1,Dept))
print(issubclass(Dept,Stud1))
