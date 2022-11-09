# Iterating through a string Using List Comprehension
name = [letter for letter in 'Mansi' ]
print(name)

# Using if with List Comprehension
even_list= [ x for x in range(20) if x % 2 == 0]
print("Even List :",even_list)

# Nested IF with List Comprehension
nums = [num for num in range(20) if num%2==0 if num > 5]
print("Even list of no. which is > 5 : ",nums)

# if - else With List Comprehension
lst = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(lst)

# matrix using Nested list comprehension
matrix = [[i for i in range(5)] for j in range(5)]
print(matrix)

# flatten of 2-D list:
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)



