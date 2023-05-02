# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
a = float(input("What is the leg length of side a?\nenter a here:"))
b = float(input("What is the leg length of side b?\nenter b here:"))

csquared = ((a**2) + (b**2))
result = math.sqrt(csquared)
print("C equals: ",result)