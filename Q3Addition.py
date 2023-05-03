# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
flag = True


x = random.randint(2,100)
y = random.randint(2,100)
sum = (x + y)
print(sum)

while flag is True:
    print("\nThis is your math problem...")
    print(x,"+",y,"=")

    z = int(input("Your Answer:"))

    if z == sum:
        print("\nCorrect Answer!")
        flag = False

    elif z == sum:
        flag = True
        break
    
    