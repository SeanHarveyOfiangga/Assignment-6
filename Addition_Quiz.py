#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

def generator1():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
            int(input(f"{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        else:
            break
def generator2():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator3():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator4():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))    
def generator5():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator6():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator7():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator8():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator9():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))
def generator10():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    int(input(f"{number1} + {number2} = "))

generator1()
generator2()
generator3()
generator4()
generator5()
generator6()
generator7()
generator8()
generator9()
generator10()