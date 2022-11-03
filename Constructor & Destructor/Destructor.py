# 1
class cls :

	def __init__(self):
		print('Employee created.')

	# Deleting(Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = cls()
del obj

# 2
class cls1:

	def __init__(self):
		print('cls1 created')
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = cls1()
	print('function end...')
	return obj

print('\nCalling Create_obj() function...')
obj = Create_obj()
print('Program End...')
