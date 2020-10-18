print("Program has started")
print("Please enter a letter:")

Character = input()

if (len(Character) == 1):
  print("The ASCII code for {} is {} ".format(Character, ord(Character)))
else:
  print("A single Character was expected")
  
print("Program ended")