#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

def intro():
    print ("\nWelcome to Addition Quiz App!")
intro()

def generator1():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 1:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            print ("Correct!")
            return answer
        else: 
            print (f"The correct answer is: {number1 + number2}")
            answer = 0
            return answer
def generator2():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 2:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator3():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 3:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator4():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 4:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer  
def generator5():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 5:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator6():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 6:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator7():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 7:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator8():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 8:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator9():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 9:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer
def generator10():
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    while True:
        try:
           answer = int(input(f"\nQuestion number 10:\n{number1} + {number2} = "))
        except ValueError:
            print ("Invalid Answer, Please Try Again.\n")
        if answer == number1 + number2:
            answer = 1
            return answer
        else: 
            answer = 0
            return answer

def total():
    first = generator1()
    second = generator2()
    third = generator3()
    fourth = generator4()
    fifth = generator5()
    sixth = generator6()
    seventh = generator7()
    eighth = generator8()
    nineth = generator9()
    tenth = generator10()
    total = first + second + third + fourth + fifth + sixth + seventh + eighth + nineth + tenth
    return total

total_score = total()

def score():
    print (f"\nYour score is: {total_score}/10")
    if total_score >= 8:
        print ("Congratulations, keep it up!")
    elif total_score >= 5 and total_score <= 7:
        print ("Good job!")
    elif total_score <= 4:
        print ("It's okay, keep on practicing.")
    print ("\nThank you for taking the quiz!")

score()
