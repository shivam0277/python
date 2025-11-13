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

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Output: ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Output: ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Output: ['apple', 'cherry']

#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#delete entire list 
del thislist

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Using a while loop:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#Output: ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Case sensitive sorting can give an unexpected result
['Kiwi', 'Orange', 'banana', 'cherry']
#Perform a case-insensitive sort of the list:
['banana', 'cherry', 'Kiwi', 'Orange']


#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#or
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]

#Join two list
list3 = list1 + list2
#or
for x in list2:
  list1.append(x)
#or
list1.extend(list2)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, 
# all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Output: ('orange', 'kiwi', 'melon')
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")


# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple 
# with the item(s), and add it to the existing tuple:
# Example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

#Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Output: apple banana cherry

#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#Output: apple ['mango', 'papaya', 'pineapple'] cherry

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


#A set is a collection which is unordered, unchangeable*, and unindexed.
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Duplicates Not Allowed
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

#Remove an item from a set, using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
#or
thisset.discard("banana")

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

#Delete the set completely:
del thisset

#Join Two Sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2

#Join set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
#Output: {'a', 1, 2, 3, 'b', 'c'} random order

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
#Output: {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
#Output: {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
#Output: {'banana', 'cherry'}
#or
set3 = set1 - set2

# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.


# Python has a set of built-in methods that you can use on sets.
# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others


# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Get a list of the keys:
x = thisdict.keys()

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#Output: dict_keys(['brand', 'model', 'year', 'color'])

#The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
#Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#or
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()


#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]

#delete the dictionary completely
del thisdict

#The clear() method empties the dictionary:
thisdict.clear()

#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():


#You can use the keys() method to return the keys of a dictionary:
# for x in thisdict.keys():


#Loop through both keys and values, by using the items() method:
#for x, y in thisdict.items():
  print(x, y)

#Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
#or
mydict = dict(thisdict)

#Nested Dictionaries
#A dictionary can also contain dictionaries, this is called nested dictionaries.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary