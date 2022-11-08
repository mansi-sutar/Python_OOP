# using user defined function
# 1.
def check(num):
    if num % 2 == 0:
          return True

    else:
          return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter(check,list1)
print(list(even_list))

# 2.
def fun(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (letter in vowels):
        return True
    else:
        return False
letters = ['f', 'a', 'm', 'j', 'e', 's', 'u', 'r']
filtered = filter(fun, letters)
print('The filtered letters are:')
for s in filtered:
    print(s)

# using lambda function
nums = [1, 2, 3, 4 , 5, 6, 8,]

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))

odds = filter(lambda x: x % 2 != 0, nums)
print(list(odds))
