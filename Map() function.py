# Using user defined function
def square(n):
	return n * n

numbers = [1, 2, 3, 4, 5]
res = map(square, numbers)
print(res)
print(list(res))

# Using user defined function and passing multiple iterator
def addition(a,b):
	return a+b

num1 = (1, 2, 3, 4)
num2 = (5, 3, 5, 6)
result = map(addition, num1,num2)
print(list(result))

# Using lambda function
# 1.
result1 = map(lambda x: x + x, numbers)
print(list(result1))
# 2.
result2 = map(lambda x, y: x + y, num1, num2)
print(list(result2))