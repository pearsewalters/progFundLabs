## Sam Walters
## Lab 2, source code
## This program displays to the user a welcome message, reads an input of the user's name,
##  gives them some options, and reads an input of their selection. It then outputs a
##  message to the screen depending on the user's input.

# 01. Display welcome message
print("Welcome! This is a computer gaming program of some sort! You'll enter your name, then make a menu selection, and be treated a lil message on the other end.")
# 02. Get user name, store it 
user_name = input("Your name: ")
# 03. Display game menu
print("1. Make Change","2. High Card","3. Quit",sep="\n")
# 04. Get user choice, store it
user_choice = int( input("Choose an option by entering the number you'd like to select. Then press enter. ") )
# 05. Display output message
print(user_name, ", you chose menu option ", user_choice, sep="", end=".")
