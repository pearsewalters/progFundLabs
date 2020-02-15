## Sam Walters
## Lab 3, source code
##
## Displays a menu with 2 dead-end options and 1 option to play the Make Change game
## Make Change calc's the difference between what a customer paid and what they owe, then
##      displays the correct amounts of denominations up to whole dollar amounts to be returned
##      to the customer


# Display game menu
print()
print('    Menu')
print('~~~~~~~~~~~~')
print("1. Make Change","2. High Card","3. Quit",sep="\n",end="\n\n")

user_choice = int( input("Choose an option: ") )

if user_choice == 1:
    print('MAKE CHANGE GAME')

    ## CONSTANTS
    DOLLAR = 1.0
    QUARTER = 0.25
    DIME = 0.1
    NICKEL = 0.05
    PENNY = 0.01

    # read for owed amt
    owed = float( input('What does the customer owe? $') )
    # read for paid amt
    paid = float( input('What did the customer pay? $') )
    # display change owed
    change = round( paid - owed, 2)

    if paid < owed:
        print('You entered an invalid amount')
    else: 
        print('$',change,sep='')

        # Calc and display dollars owed
        dollar_remainder = round( change % DOLLAR, 2 )
        dollars_back = round( ( change - dollar_remainder) / DOLLAR, 2 )
        if dollars_back > 0:
            if dollars_back > 1:
                print( int(dollars_back), 'dollars' )
            else:
                print( int(dollars_back), 'dollar' )

        # Quarters...
        quarter_remainder = round( dollar_remainder % QUARTER, 2 )
        quarters_back =  round( ( dollar_remainder - quarter_remainder ) / QUARTER, 2)
        if quarters_back > 0:
            if quarters_back > 1:
                print( int(quarters_back), 'quarters' )
            else:
                print( int(quarters_back), 'quarter' )

        # Dimes...
        dime_remainder = round( quarter_remainder % DIME, 2 )
        dimes_back = round( ( quarter_remainder - dime_remainder ) / DIME, 2 )
        if dimes_back > 0:
            if dimes_back > 1:
                print( int(dimes_back), 'dimes' )
            else:
                print( int(dimes_back), 'dime' )

        # Nickels...
        nickel_remainder = round( dime_remainder % NICKEL, 2 )
        nickels_back = round( ( dime_remainder - nickel_remainder) / NICKEL, 2 )
        if nickels_back > 0:
            if nickels_back > 1:
                print( int(nickels_back), 'nickels' )
            else:
                print( int(nickels_back), 'nickel' )

        # Pennies
        penny_remainder = round( nickel_remainder % PENNY, 2 )
        pennies_back = round( ( nickel_remainder - penny_remainder) / PENNY, 2 )
        if pennies_back > 0:
            if pennies_back > 1:
                print( int(pennies_back), 'pennies' )
            else:
                print( int(pennies_back), 'penny' )
        # end handling change
    # end make change game
elif user_choice == 2:
    print('High Card is coming soon!')
elif user_choice < 1 or user_choice > 3:
    print('That was an invalid selection! :(')
