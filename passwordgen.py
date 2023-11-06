#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#Defining the variables
unscrambled = ""
scrambled = ""
random_letter = len(letters) - 1
random_symbol = len(symbols) - 1
random_number = len(numbers) - 1

#Selecting the random characters
for letter in range(1, nr_letters +1):
  unscrambled += (letters[random.randint(0,random_letter)])
  unscrambled += " "
for symbol in range(1, nr_symbols +1):
  unscrambled += (symbols[random.randint(0,random_symbol)])
  unscrambled += " "
for number in range(1, nr_numbers +1):
  unscrambled += (numbers[random.randint(0,random_number)])
  unscrambled += " "

#Shuffling the character order
unscrambledlist = unscrambled.split()
random.shuffle(unscrambledlist)

for character in unscrambledlist:
  scrambled += character

print(f"Your password is: {scrambled}")
