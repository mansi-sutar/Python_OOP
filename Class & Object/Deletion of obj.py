class Emp:
    id = 201
    name = "Riya"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp = Emp()

# Deleting the property of object
del emp.id
# Deleting the object itself
del emp
emp.display()
