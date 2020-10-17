print("how many live cables should I avoid?")
Livecables = int(input())

Numberofcables = 0 

print("")
while (Livecables > Numberofcables):
    print("Avoiding...", end="")
    Numberofcables = Numberofcables + 1
    print("Done!", Numberofcables, "cables avoided.")