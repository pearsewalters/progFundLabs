## Sam Walters
## Lab 2, source code
## This program displays to the user a welcome message, reads an input of the user's name,
##  gives them some options, and reads an input of their selection. It then outputs a
##  message to the screen depending on the user's input.

# Display welcome message
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("| Welcome! This is the Lame Games Room! |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Get user name, store it 
user_name = input("Say, what's your name? ")

# Display game menu
print()
print('    Menu')
print('~~~~~~~~~~~~')
print("1. Make Change","2. High Card","3. Quit",sep="\n",end="\n\n")
# Get user choice, store it
user_choice = int( input("Choose an option: ") )
# Display output message
print(user_name, ", you chose menu option ", user_choice, sep="", end=".")
