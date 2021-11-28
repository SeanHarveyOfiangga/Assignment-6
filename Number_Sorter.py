#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

def intro():
    print ("\nWelcome to Number Sorter app!")

intro()

First = int(input("\nPlease enter your first number: "))
Second = int(input("Please enter your Second number: "))
Third = int(input("Please enter your Third number: "))
Fourth = int(input("Please enter your Fourth number: "))

def Numbers():
    if First >= Second and First >= Third and First >= Fourth:
        One = First
        if Second >= Third and Second >= Fourth:
            Two = Second
            if Third >= Fourth:
                Three = Third
                Four = Fourth
                print (f"The highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!")
                exit()
            if Fourth >= Third:
                Three = Fourth
                Four = Three
                print (f"The highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!")
                exit()
        if Third >= Second and Third >= Fourth:
            Two = Third
            if Second >= Fourth:
                Three = Second
                Four = Fourth
                print (f"The highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!")
                exit()
            if Fourth >= Second:
                Three = Fourth
                Four = Second
                print (f"The highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!")
                exit()
        if Fourth >= Second and Fourth >= Third:
            Two = Fourth
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
