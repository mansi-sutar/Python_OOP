class Emp:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

s = Emp("Riya", 101, 20000)

# To access the attribute of the object.
print(getattr(s, 'name'))
print(getattr(s, 'id'))
print(getattr(s, 'salary'))

# To set a particular value to the specific attribute of an object.
setattr(s, "salary", 30000)

# modified value of age
print(getattr(s, 'salary'))

# returns true if the object contains some specific attribute.
print(hasattr(s, 'id'))

# To delete a specific attribute.
delattr(s, 'salary')

print(s.salary)