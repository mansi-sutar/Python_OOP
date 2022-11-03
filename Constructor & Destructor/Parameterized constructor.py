# 1
class cls:
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name
    def show(self):
        print("Hello",self.name)
c = cls("Riya")
c.show()

# 2
class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print("\nFirst no. = " + str(self.num1))
        print("Second no. = " + str(self.num2))
        print("Result :  = " + str(self.res))

    def calculate(self):
        self.res = self.num1 + self.num2

obj = Add(500, 300)
obj.calculate()
obj.display()


