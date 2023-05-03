# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
def main():

    import random
    flag = True

    x = random.randint(2,100)
    y = random.randint(2,100)
    sum = (x + y)

    while flag is True:
        print("\nThis is your math problem...")
        print(x,"+",y,"=")
        print(sum)

        z = (input("Your Answer:"))

        if z.isnumeric() is False:
            print("\nInvalid, must be an Integer")
        
        elif int(z) == sum:
            print("\nCorrect Answer!\n")
            flag = False
            main2()

        elif int(z) == sum:
            flag = True
            break

        elif int(z) != sum:
            print("\nIncorrect, try again")
    
def main2():

    while True:
        r = input("Would you like another question?\nYes/No: ")

        capr = str.upper(r)
        if capr == "YES" or capr == "Y":
            main()
        elif capr == "NO" or capr == "N":
            print("\nOk then, Have a good one!\n")
            exit()
        
        else:
            print("\nPlease answer with yes or no\n")
            main2
main()