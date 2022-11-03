# Simple Class
class cls:
    a,b= 10,30
    print("a + b =", a+b)

# Class & Object
class emp:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Name : ", self.name)
        print("Id :", self.id)
        print("Salary",self.salary)


c1 = emp("Riya", 808, 30000)
c1.display()

# self parameter
class Employee:
    id = 101
    name = "Mansi"
    def display (self):
        print("ID: %d \nName: %s"%(self.id,self.name))
emp = Employee()
emp.display()


