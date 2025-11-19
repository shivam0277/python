x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# Global variable
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300
def myfunc():
  global x
  x = 200

myfunc()

print(x)
# Output: 200


# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


# Python follows the LEGB rule when looking up variable names, and searches for them in this order:
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace




print("Hello"); print("How are you?"); print("Bye bye!")


print("Hello World!", end=" ")
print("I will print on the same line.")


#Arithmetic Operators
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b)
# Output: 13 7 30 3.33333333333


x = 2
print(x ** 5)
# Output: 32

name = "AI"
print(name + " Rocks! " * 2)
# Output: AI Rocks! AI Rocks!


s = "Python"
print(s[1:4])   # Output: yth
print(s[::-1])  # Output: nohtyP

#list comprehension
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

#conditional list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8]


#dictionary access
person = {"name": "Alice", "age": 25}
print(person["name"])       # Output: Alice
print(person.get("age"))    # Output: 25


squares_dict = {x: x**2 for x in range(4)}
print(squares_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9}


a, b, c = (1, 2, 3)
print(a + b + c)
# Output: 6


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2, set1 & set2, set1 - set2)
# Output: {1, 2, 3, 4, 5} {3} {1, 2}





print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")

    