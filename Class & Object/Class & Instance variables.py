# Instance variables are for data, unique to each instance
# class variables are for attributes and methods shared by all instances of the class

class Data:

    # Class Variable
    dept = 'Devp'

    # The init method or constructor
    def __init__(self, id, name,salary):
        # Instance Variable
        self.id = id
        self.name = name
        self.salary =salary

emp1 = Data(101,"Mansi",10000)
emp2 = Data(102,"Riya",10000)

print('Details od emp1:')
print('Dept. :', emp1.dept)
print('ID :', emp1.id)
print('Name :', emp1.name)
print('Salary :', emp1.salary)

print('\nDetails od emp2:')
print('Dept. :', emp2.dept)
print('ID :', emp2.id)
print('Name :', emp2.name)
print('Salary :', emp2.salary)



print("\nAccessing class variable using class name")
print(Data.dept)