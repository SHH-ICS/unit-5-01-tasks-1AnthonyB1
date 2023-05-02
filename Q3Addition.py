# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
while True:
    a = (input("What is the number at the start of your series?\nenter a here:"))
    if a.isnumeric() is False:
        print("\nInvalid, please try again with a number:\n")
    elif a.isnumeric() is True:
        break

while True:
    b = (input("What is the number at the start of your series?\nenter b here:"))
    if b.isnumeric() is False:
      print("\nInvalid, please try again with a number:\n")
    elif b.isnumeric() is True:
        break

c = (int(a) + 1)

x = random.randint(int(c),int(b))
print("\nThis is a rendom number in between,", int(a), "and", int(b),":", x)
