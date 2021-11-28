#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

#intro
def intro():
    print ("\nWelcome to Number Sorter app!")

intro()

#user input
while True:
    try:
        First = int(input("\nPlease enter your first number: "))
        Second = int(input("Please enter your Second number: "))
        Third = int(input("Please enter your Third number: "))
        Fourth = int(input("Please enter your Fourth number: "))
    except ValueError:
        print ("Sorry, input numbers only.")
    else:
        break

#sorter function
def Sorter():
    #if the first number is the highest number
    if First >= Second and First >= Third and First >= Fourth:
        One = First
        #if the second number is the second highest number
        if Second >= Third and Second >= Fourth:
            Two = Second
            #if the third number is the third highest number
            if Third >= Fourth:
                Three = Third
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= Third:
                Three = Fourth
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the third number is the second highest number        
        if Third >= Second and Third >= Fourth:
            Two = Third
            #if the second number is the third highest number
            if Second >= Fourth:
                Three = Second
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= Second:
                Three = Fourth
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the fourth number is the second highest number
        if Fourth >= Second and Fourth >= Third:
            Two = Fourth
            #if the second number is the third highest number
            if Second >= Third:
                Three = Second
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the third number is the third highest number
            if Third >= Second:
                Three = Third
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
    #if the second number is the highest number
    elif Second >= First and Second >= Third and Second >= Fourth:
        One = Second
        #if the first number is the second highest number
        if First >= Third and First >= Fourth:
            Two = First
            #if the third number is the third highest number
            if Third >= Fourth:
                Three = Third
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= Third:
                Three = Fourth
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the third number is the second highest number
        if Third >= First and Third >= Fourth:
            Two = Third
            #if the first number is the third highest number
            if First >= Fourth:
                Three = First
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= First:
                Three = Fourth
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the fourth number is the second highest number        
        if Fourth >= Third and Fourth >= First:
            Two = Fourth
            #if the first number is the third highest number
            if First >= Third:
                Three = First
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the third number is the third highest number
            if Third >= First:
                Three = Third
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
    #if the third number is the highest number
    elif Third >= First and Third >= Second and Third >= Fourth:
        One = Third
        #if the first number is the second highest number
        if First >= Second and First >= Fourth:
            Two = First
            #if the second number is the third highest number
            if Second >= Fourth:
                Three = Second
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= Second:
                Three = Fourth
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the second number is the second highest number
        if Second >= First and Second >= Fourth:
            Two = Second
            #if the first number is the third highest number
            if First >= Fourth:
                Three = First
                #if the fourth number is the lowest number
                Four = Fourth
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the fourth number is the third highest number
            if Fourth >= First:
                Three = Fourth
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the fourth number is the second highest number
        if Fourth >= Second and Fourth >= First:
            Two = Fourth
            #if the first number is the third highest number
            if First >= Second:
                Three = First
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the second number is the third highest number
            if Second >= First:
                Three = Second
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
    #if the fourth number is the highest number
    elif Fourth >= First and Fourth >= Third and Fourth >= Second:
        One = Fourth
        #if the first number is the second highest number
        if First >= Third and First >= Second:
            Two = First
            #if the third number is the third highest number
            if Third >= Second:
                Three = Third
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the second number is the third highest number
            if Second >= Third:
                Three = Second
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the third number is the second highest number        
        if Third >= First and Third >= Second:
            Two = Third
            #if the first number is the third highest number
            if First >= Second:
                Three = First
                #if the second number is the lowest number
                Four = Second
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the second number is the third highest number
            if Second >= First:
                Three = Second
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        #if the second number is the second highest number
        if Second >= Third and Second >= First:
            Two = Second
            #if the first number is the third highest number
            if First >= Third:
                Three = First
                #if the third number is the lowest number
                Four = Third
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
            #if the third number is the third highest number
            if Third >= First:
                Three = Third
                #if the first number is the lowest number
                Four = First
                print (f"\nThe highest number is '{One}', then '{Two}', then '{Three}', and the lowest number is '{Four}.'")
                print ("\nThank you for using Number Sorter App!\n")
                exit()
        
Sorter()
