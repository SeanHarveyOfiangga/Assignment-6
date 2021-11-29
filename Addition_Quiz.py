#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

number1 = random.randint(0,99)
number2 = random.randint(0,99)

for i in range (10):
        int(input(f"{number1} + {number2} = "))