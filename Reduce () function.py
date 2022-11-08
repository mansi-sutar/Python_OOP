import functools
from functools import reduce
# Using user defined function
def do(x,y):
    return x+y
num1 = [1,2,3,4,5]
sum = reduce(do,num1)
print("Sum of num1 is : ",sum)

# Using lambda function
num2 = [1, 2, 3, 4, 5]
# 1. Sum
print("sum of elements is : ")
print(functools.reduce(lambda a, b: a+b, num2))

# 2. maximum element from list
print("Maximum element is : ")
print(functools.reduce(lambda a, b: a if a > b else b, num2))

# Minimum element from list
print("Minimum element is : ")
print(functools.reduce(lambda a, b: a if a < b else b, num2))

# filter() within map()
lst = [1,2,9,10,5,6,7,8]
num = map(lambda x:x+1,filter(lambda x:x>5,lst))
print("New list :",list(num))

# map() with filter()
num = filter(lambda x: x>5,map(lambda x: x+1,lst))
print("New list :",list(num))

# map() & filter() within reduce()
res = reduce(lambda x,y:x+y,map(lambda x:x+x , filter(lambda x:x<5,lst)))
print("Result is : ",res)



