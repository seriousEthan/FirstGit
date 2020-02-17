#Ethan Martin
#Module 3

#Variables
names = ["Marie", "Sassy", "Abby", "Tia", "Kailani", "XavierIII"]
FLnames = [{"First": "Marie", "Last": "Strouf"}, {"First": "Sassy", "Last": "Strouf"}, {"First": "Abby", "Last": "Stewart"},
           {"First": "Tia", "Last": "McBee"}, {"First": "Kailani", "Last": "Brown"}, {"First": "Xavier", "Last": "Brown III"}]
Numbers = [(1, 2), (6, 9), (5,8)]
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = (21, 22, 23, 24, 25)

#1.1

for inputName in names:
    print("Hi there,", (inputName), ".")
    print((inputName), ", you are secretly my favorite family member .")
    print("Don't tell anyone else that,", (inputName),".")
    print("----------------------------------------------------------------")



#1.2

for inputName in FLnames:
    first= inputName["First"]
    last= inputName["Last"]
    print("Hi there", first, last, "did you know that you're my hero?")
    print(first, last, "did you know that you're everything I wish to be?")
    print(first, last, "did you know that you're the wind beneath my wings?")
    print("---------------------------------------------------------------- ")

#1.3

for inputNum in Numbers:
    sum = inputNum[0] + inputNum[1]
    print("Math is fun! When you add", inputNum[0], "to", inputNum[1], "the result is", sum, ".")
    print("-----------------------------------------------------------------")

#1.4

def returnCalc(inputNum):
    sum = inputNum[0] + inputNum[1]
    return sum

for sumReturn in Numbers:
    sum = returnCalc(sumReturn)
    print("Math is fun! When you add", sumReturn[0], "to", sumReturn[1], "the result is", sum, ".")
    print("-----------------------------------------------------------------")

#2
# pow(16,(1/2)) was the original expression we were told to fix.  If you wrap it in a print call then it yields
# 4.0.  That should be correct.  I assume the answer was the wrong "class", so I changed it to an integer with the
# following call/function.
print("The answer to question 2 is",int(pow(16,(1/2))))

#3

print("A) The value of 3*x =", str(x * 3))
print("B) The value of x+y =", str(x + y))
print("C) The value of x-y can not be calculated using lists")
print("D) The value of x[1] =", str(x[1]))
print("E) The value of x[0] =", str(x[0]))
print("F) The value of x[-1] =", str(x[-1]))
print("G) The value of x[:] =", str(x[:]))
print("H) The value of x[2:4] =", str(x[2:4]))
print("I) The value of x[1:4:2] =", str(x[1:4:2]))
print("J) The value of x[:2] =", str(x[:2]))
print("K) The value of x[::2] =", str(x[::2]))
x[3]=8
print(x)
print("L) When you run x[3]=8, which I just did,  Python changes the number in position 3 (the fourth position since it starts at 0) to an 8")
print("the number was originally a 4. so the new list looks like [1, 2, 3, 8, 5] instead of [1, 2, 3, 4, 5]")
print("M) This is impossible because the values in a tuple cannot be changed.")




