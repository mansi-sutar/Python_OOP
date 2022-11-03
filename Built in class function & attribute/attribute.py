class Emp:
    'Employee Details...!!!'
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

s = Emp("Riya", 101, 20000)

# contains a string which has the class documentation
# print(Emp.__doc__) using cls name
print(s.__doc__)

# dictionary containing the information about the class namespace.
print("\n",s.__dict__)

# To access the module in which, this class is defined.
print("\n",s.__module__)

# To access the class name.
print("\n",Emp.__name__)

# contains a tuple including all base classes.
print("\n",Emp.__base__)

