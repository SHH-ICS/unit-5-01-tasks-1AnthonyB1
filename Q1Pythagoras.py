# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

while True:
    a = (input("\nWhat is the leg length of side a?\nenter a here:"))
    if a.isnumeric() is False:
        print("\nInvalid, please try again with a number:")
    elif a.isnumeric() is True:
        break

while True:
    b = (input("\nWhat is the leg length of side b?\nenter b here:"))
    if b.isnumeric() is False:
        print("\nInvalid, please try again with a number:")
    elif b.isnumeric() is True:
        break

csquared = ((float(a)**2) + (float(b)**2))
result = math.sqrt(csquared)
print("\nC equals: ",result)