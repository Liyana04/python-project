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

# list methods
numbers = [5,2,1,5,8,9,4]
# print(numbers.append(20)) will add at the end of the list
# print(numbers.insert(0,10)) will add 10 at index 0 of the list
# print(numbers.remove(5)) will remove number 5
# print(numbers.clear()) will cler all the list []
# print(numbers.pop()) will return last number which is 4
# print(numbers.index(5)) will return the index of number 5
# print(50 in numbers) will return False
# print(number.count(5)) will return 2 since there are two 5
# to sort list
# numbers.sort() akan susun ascending order
# numbers.revers()
# print(numbers)
# remove duplicate numbers
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
# will return [2,4,6,3,1]

# tuples. cannot add or change anything in the list
numbers =(1,2,3)
numbers[0] = 10
# print(numbers[0]) will return error, sbb tuple cannot change at all

# unpacking
# coordinates = (1,2,3) can use [1,2,3] too
# x,y,z = coordinates
# print(y) will return 1 and so on..

# dictionary
customer = {
    "name": "John Smith",
    "age": 21,
    "is_verified": True
}
# print(customer['name']) can use this or
# print(customer.get("name")) will return None
customer["name"] = "Jack Snow"
print(customer.get("birthdate", "Jan 1 2003"))

# map dictionary
phone = input("Phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!")+ " "
print(output)
# ! if cannot find in the digit_mapping

# emoji converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) +" "
    # second word act as default value like ! above
print(output)

# functions
# def means define function
def greet_user(first_name, last_name):
    print(f'Hello {first_name}{last_name}!')
    print('Welcome abroad')

# need to add 2 lines break after defining function
print("Start")
# parameters
# greet_user("John","Smith") position argument first
# calc_cost(total=50, shipping=5, discount=0.1) keyword argument second
print("Finish")

# return value
def square(number):
    return number * number
result = square(3)
print(result)

# creating a reusable function
def emoji_converter(message):
    
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) +" "
        # second word act as default value like ! above
    return output


message = input(">")
result = emoji_converter(message)
print(result)

# exception
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Value!')

#class
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point1 = Point()

# constructors
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point=Point(10,20)
print(point.x)
# return 10
point.x =11
print(point.x)
# return 11

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")
        print(f"Hi!, I' am {self.name}")


john = Person("John Smith")
# print(john.name)
john.talk()

bob = Person("Bob Joe")
bob.talk()

# inheritance
class Dog:
    def walk(self):
        print("walk")

# repeated with above class
class Cat:
    def walk(self):
        print("walk")

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()

# modules(use other file, converters.py and utils.py)
# just import from other file then use . the function
import converters
converters.kg_to_lbs
print(converters.kg_to_lbs(70))

# or can use this way(ctrl + space)
from converters import kg_to_lbs
print(kg_to_lbs(100))

# find max number from module above
from utils import find_max

numbers = [10,3,6,2]
max = find_max(numbers)
# actually max already build in python function
# just print(max(numbers))
print(max)
