#Slicing 
b = "Hello, World!"
print(b[-5:-2])
#Output: orl

b = "Hello, World!"
print(b[:5])
#Output: Hello


#Modify String

#strip() method removes any whitespace from the beginning or the end:
# isalpha() to check if all characters in a string are alphabets and is not empty.
# isalnum() to check if all characters in a string are alphanumeric (letters and numbers) and is not empty.
# isdecimal() to check if all characters in a string are decimal characters and is not empty.
# lower() to convert all characters in a string to lowercase.
# islower() to check if all characters in a string are lowercase.
# upper() to convert all characters in a string to uppercase.
# isupper() to check if all characters in a string are uppercase.
# title() to convert the first character of each word in a string to uppercase.
# startswith() to check if a string starts with a specified substring.
#replace() method replaces a string with another string:
# split() method splits the string into substrings if it finds instances of the separator

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.isalpha())
print(a.isalnum())
print(a.isdecimal())
print(a.replace("H", "J"))
print(a.split(","))

#String concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Output: Hello World


age = 36
txt = "My name is John, I am " + str(age)
print(txt)

#OR

age = 36
txt = f"My name is John, I am {age}"    #use of f string
print(txt)


#A placeholder can include a modifier or hold arithmatic operations etc to format the value. Curly brackets 
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed 
# point number with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#Output: We are the so-called "Vikings" from the north.


#boolean
print(bool("Hello")) #both are true
print(bool(15))

print(bool(False)) #all are false
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


x = 200
print(isinstance(x, int))

#Arithmatic Operators(Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, Floor Division)
x = 15
y = 2
print(x // y) #Output:7  (Floor Division)
#  / gives float result
#  // gives integer result 


#The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
#Output:
#True False True


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note:There are some list methods that will change the order, but in general: the order of the items will not change.

# Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


#A list with strings, integers and boolean values
list1 = ["abc", 34, True, 40, "male"]

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Example : Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Output: ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Output: ['orange', 'kiwi', 'melon']

#Change Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)