#Match Case Example
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
#Output: A weekday in May


# With the break statement we can stop the loop even if the while condition is true:
# Example:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#Output: 1 2 3


# With the continue statement we can stop the current iteration, and continue with the next:
# Example:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#Output: 1 2 4 5 6


#Python functions

#To call a function, write its name followed by parentheses:
def my_function():
  print("Hello from a function")

my_function()


# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
  pass


#Passing Arguments to a Function
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, 
# just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first 
# name, which is used inside the function to print the full name:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

#You can assign default values to parameters. If the function is called without an argument, it uses the 
# default value

# Keyword Arguments
# You can send arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


# Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#A function that returns a list:
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#A function that returns a tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#To specify positional-only arguments, add , / after the arguments:
# def my_function(name, /)
#To specify that a function can have only keyword arguments, add *, before the arguments:
# def my_function(*, name)
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only



# *args and **kwargs
# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:
# Using *args to accept any number of arguments:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#Arbitrary Arguments are often shortened to *args in Python documentation.

#Accessing individual arguments from *args:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#You can combine regular parameters with *args.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


#A function that calculates the sum of any number of values:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before 
# the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Using **kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


# The order must be:
# regular parameters
# *args
# **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")



#Decorators - Advance topic

#Lambda Functions
#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def my_function(n):
  return lambda a : a * n


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mytripler(11))
print(mydoubler(11))

#Use lambda functions when an anonymous function is required for a short period of time.

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
# Using Lambda with map()
# The map() function applies a function to every item in an iterable:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# The filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
# Output: ['pie', 'apple', 'banana', 'cherry'] 

#Recursion
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


#Generators
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

# The yield keyword is what makes a function a generator.
# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator 
# is called, it continues from where it left off.
#Generator saves memory

