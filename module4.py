#Ethan Martin
#Module 4

#import library
import math
#Make sure it is running correctly
print("If this is working correctly it will be able to calculate that the sqrt of 4 is 2")
print("The computer thinks the answer is", math.sqrt(4), "because the result is a float.")
print("---------------------------------------------------------------------------------")
#Problem 1 Roots

def main():
    print("This program finds the real solutions to a quadratic equation based on user input")
    print()
a,b,c = eval(input("Please enter the coefficients (a, b, c,):"))

discRoot = math.sqrt(b**2 - 4*a*c)
root1 = ((-b + discRoot)/(2 * a))
root2 = ((-b - discRoot)/(2 * a))
print()

main()
print("The solutions to the quadratic equation are:", root1, root2)
print("---------------------------------------------------------------------------------")
#Problem 2 Reciprocals

#List of fractions for the problem
fractions = [('1/2', 1/2), ('1/3', 1/3), ('1/4', 1/4), ('1/5', 1/5), ('1/6', 1/6), ('1/7', 1/7), ('1/8', 1/8), ('1/9', 1/9), ('1/10', 1/10)]
#Solution
print("I will use a for loop to print the decimal representations of 1/2, 1/3, ..., 1/10, one on each line.")
for number in fractions:
    print()
    print(number)

