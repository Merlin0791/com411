print("Program has started")
print("Please enter a Value:")

value = abs(int(input()))

if (value >= 32 and value <= 126):
  print("The ASCII code for {} is {} ".format(value, chr(value)))
else:
  print("invalid number!")

print("Program ended!")