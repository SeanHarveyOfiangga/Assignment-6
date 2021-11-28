#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

def intro():
    print ("\nWelcome to number sorter app!")

intro()

First = int(input("\nPlease enter your first number: "))
Second = int(input("Please enter your Second number: "))
Third = int(input("Please enter your Third number: "))
Fourth = int(input("Please enter your Fourth number: "))

def Numbers():
    if First >= Second and First >= Third and First >= Fourth:
        One = First
        print (One)
    elif Second >= First and Second >= Third and Second >= Fourth:
        One = Second
        print (One)
    elif First >= First and First >= Second and First >= Fourth:
        One = Third
        print (One)
    elif Fourth >= First and Fourth >= Third and Fourth >= Second:
        One = Fourth
        print (One)
Numbers()
