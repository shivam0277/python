import random  

# def get_choices():
#   player_choice = "rock"
#   computer_choice="paper"

#   return player_choice

# def greeting():
#   return "Hi"

# response = greeting()
# print(response)

# choices = get_choices()
# print(choices)

def get_choices():
   options = ["rock", "paper", "scissors"]
   player_choice = input("Enter your choice(Rock, Paper, Scissors): ")
   computer_choice = random.choice(options)
   choices = {"player": player_choice, "computer":computer_choice}
   return choices

# choice = get_choices()
# print(choice)

def determine_winner(player, computer):
   print(f"You chose {player} and the computer chose {computer}")
   if player == computer:
      return "Its a tie!"
   elif (player == "rock"):
        if computer == "scissors":
             return "Rock smashes scissors! You win!"
        else:
             return "Paper covers rock! You lose!"
   elif (player == "paper"):
        if computer == "scissors":
             return "scissors cuts paper! You lose!"
        else:
             return "Paper covers rock! You win!"
   elif (player == "scissors"):
        if computer == "paper":
             return "scissors cuts paper! You win!"
        else:
             return "Rock smashes scissors! You lose!"
   
choices = get_choices()
result = determine_winner(choices["player"], choices["computer"])
print(result)


# determine_winner("rock", "paper")


# age = 25
# print(f"my age is {age}")  //called f string


print("Shivam is Tight".title())
name = "Shi\vam" #escape sequence


#Classes

class Animal:
     def walk(self):
          print("walk")
class Dog(Animal):

     def __init__(self,name,age):
          self.name = age
          self.age = 5

     def bark(self):
          print("Woof!")

roger = Dog("Roger", 3)
print(roger.name)
print(roger.bark())
print(roger.walk())


# modules
#to use a module we have to import it first
#we can use inbuilt modules or we can create our own modules
#example :
# import dog from animal
# dog.bark()

# import math
# print(math.sqrt(16))
# print(math.ceil(2.3))