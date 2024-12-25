print("Nur Liyana")
# can put "" or'' 
# python is capital/lowe case sensitive
print('*' * 10)
price = 10
price = 20
is_true = False
print(price)

# new practise
# name = input('What is your name? ')
# color = input('What is your favourite color? ')
# print('Hi ' + name + ' ,you like ' + color + 'color')

# new practise
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2024 -int(birth_year)
# print(type(age))
# # int()
# # bool()
# # float()
# print(age)

# new practise
# weight_lbs = input('Weight(lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# new practise
# course = "Python's Course for Beginners"
# # or can write like this
# course_1 ='Python Course for "Beginners"'
# # or can write like this for multiple line
# course_2 ='''
# Hello John,

#  Here is our first email.

# Regards,
# Yana
# '''
# another = course[:]
# name = 'Jennifer'
# # print(name[1:-1]) will output ennife  
# print(course)
# # print(course[0]) will output P or course[-1] will output s or course[0:3] will output Pyt

# formatted string practise
# first = 'John'
# last = 'Smith'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# string methods
course = 'Python for Beginners'
print(len(course))
# for upper case print(course.upper())
# for lower case print(course.lower())
# for finding the index of the character print(course.find('P')) will output 0
# for finding the index of the character print(course.find('Beginners')) will output 11, start with 'B'
# for replace 'Beginners' to 'Absolute Beginners' print(course.replace('Beginners', 'Absolute Beginners'))
# for checking if 'Python' exist in course? print('Python' in course)

#arithmetic operations
print(10/3)
# will return float, power using **
print(10//3)
# will return integer of the first number in float answer

# if statements
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water :)")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes :)")
else:
    print('It is a lovely day!')
    print('Enjoy your day!')




