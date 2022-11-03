# 1
class cls1:
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)
c1 = cls1()
c1.show("Riya")

# 2
class cls:
	def __init__(self):
		self.name = "Priya"

	def display(self):
		print("\n",self.name)

obj = cls()
obj.display()