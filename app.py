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

price = 100000
has_good_credit = True
has_high_income = True
has_criminal_record = True

# can use 'and' or 'or' or 'not' operator
if has_good_credit and not has_criminal_record:
    down_payment = 0.1 * price
    print('Eligible for loan')

# if has_high_income and has_good_credit:
#     down_payment = 0.1 * price
#     print('Eligible for loan')
# else  
#  
# if has_good_credit:
#     down_payment = 0.1 * price
#     print('Eligible for loan')
# else
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')

# comparison operator
name = 'John Smith'

if len(name) < 3:
    print("Name must be at least 5 characters")
if len(name) > 50:
    print("Maximum name is 50 characters long")
else:
    print("Name looks good!")

# weight converter program
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pound")

# while loops
i = 1
while 1 <= 5:
    print('*'*i)
    i = i + 1
print("Done")

# guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failed!')

#car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
        print("Car sopped...")
    elif command == "help":
        # python is case sensitive and space sensitive
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == quit:
        break
    else:
        print("Sorry, I don't understand that")

#for loops
# for item in range(5, 10, 2):
# for item in 'Python':
# for item in['Mosh', 'John', 'Sarah']
# for item in [1,2,3,4,5,6,7,8,9]:
# for item in range (10):
# for item in range(5,10,2): 2 means two numbers after 5 which is 5,7,9
prices =[10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#nested loops
numbers = [5,2,5,2,2]
# can use this to print F shape
for x_count in numbers:
    print('x' * x_count)
# or this to print F shape
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
# or this to print L shape
numbers = [1,1,1,1,1,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# lists
names = ['John', 'Sarah', 'May', 'Kely', 'Ray', 'Taylor', 'Zack']
# print(names[2:]) will print from May till the end
# find biggest number in the list
numbers = [3,55,4,66,5,123,6,9,8,55,3,0]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2d lists
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for row in matrix:
    for item in row:
        print(item)

