# square of no. using dictionary comprehension
square_dict = {num: num*num for num in range(1, 11)}
print("Square of no.s :",square_dict)

# Using if condition
stud = {'Mansi': 80, 'Riya': 90, 'Priya': 75, 'Siya': 88}
above_eighty = {k: v for (k, v) in stud.items() if v>=80}
print("List of above 80 % :",above_eighty)

# Using if-else Condition
persons = {'Mansi': 21, 'Riya': 25, 'Priya': 41, 'Siya':30, 'Jiya':43}
lst = {k: ('old' if v > 40 else 'young') for (k, v) in persons.items()}
print(lst)

years = [['January', 'February', 'March'], ['April', 'May', 'June'], ['July', 'August', 'September'],['October','November','December']]
years = [years for sublist in years for years in sublist if len(years) <= 5]
print(years)









