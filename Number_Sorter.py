#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

def intro():
    print ("\nWelcome to number sorter app!")

intro()

def numbers():
    First = int(input("\nPlease enter your first number: "))
    Second = int(input("Please enter your Second number: "))
    Third = int(input("Please enter your Third number: "))
    Fourth = int(input("Please enter your Fourth number: "))
    print (f"You picked: {First}, {Second}, {Third}, {Fourth}")
numbers()