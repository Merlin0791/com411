import random

print("\nPlease enter the minimum value:")
min_value = int(input())

print("\nPlease enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print("\nI am thinking of a number between {} and {}.".format(min_value, max_value))
print("\nCan you guess what it is?")

guess = 0

while(guess != random_number):
  print("\nPlease enter a number:")
  guess = int(input())

  if (guess == random_number):
    print("Congratulations!")
    break
  elif (guess < random_number):
    print("\nGuess higher")
  else:
    print("\nGuess lower")
  
print("\nGame over!")