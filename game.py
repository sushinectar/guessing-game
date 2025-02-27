# IMPORTING METHOD
import random

# NUMBER TO BE DRAWN
num_random = random.randint(1, 10) 

# INCREMENT
c = 0

print("\n-------------------------------------------\n")

print("A number from 1 to 10 was drawn! \n")

print("-------------------------------------------\n")

while True:
  num_user = int(input("Enter an integer number to try to guess: "))
  c += 1

  if num_user < num_random:
    print("Your number is greater than the drawn number. Try again :( \n")

  elif num_user > num_random:
    print("Your number is less than the drawn number. Try again :( \n")

  elif num_user > 10:
    print("Don't be a cheater! \n")

  elif num_user < 1:
    print("Don't be a cheater! \n")

  else:
    print("You got it!")
    break
