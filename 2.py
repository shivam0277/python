#data type

name = "Shivam"
print(type(name))  # Output: <class 'str'>
print(isinstance(name, str))  # Output: True

age = 25
print(type(age))  # Output: <class 'int'>
print(isinstance(age, int))  # Output: True

number = "25"
age = int(number)
print(type(age))  # Output: <class 'int'> 


#while loop
# Print numbers from 1 to 5 using while loop
num = 1
while num <= 5:
    print(num)
    num += 1
# Output: 1 2 3 4 5


# Stop when number is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2


# Skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5


#basic try and except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Invalid input! Please enter a valid number.")


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")   # runs only if no exception
finally:
    print("Program finished.")      # runs no matter what

# for input 2
# 5.0
# Division successful!
# Program finished.







