class Clg:
	def func1(self):
		print("This function is Base class.")


class Dept(Clg):
	def func2(self):
		print("This is derived cls which inherits clg.")


class Stud1(Dept,Clg):
	def func3(self):
		print("This id stud1 class which inherits dept n clg class.")


class Stud2(Dept,Clg):
	def func4(self):
		print("This id stud1 class which inherits dept n clg class.")

S2 = Stud2()
S2.func1()
S2.func2()
S2.func4()
