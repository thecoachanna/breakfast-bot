# Refactoring Breakfast Bot

# The code is more repetitive than it needs to be
# The code is overly complex or difficult to read
# The code is hard to maintain or modify
# The code is hard to re-use

import time

def print_pause(print_message):
    print(print_message)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        # Get input and use it to determine what happens next
        response = input(prompt).lower()
        # Be flexible with the input the user can enter
        if option1 in response:
            break
        elif option2 in response:
            break
        # Handle bad input without crashing
        else:
            print_pause("Sorry, I don't understand.")
    return response

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available:")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    # Get input and use it to determine what happens next
    response = valid_input("Please place your order. Would you like waffles or pancakes?\n", "waffles", "pancakes")
    # Be flexible with the input the user can enter
    if 'waffles' in response:
        print_pause("Waffles it is!")
    elif 'pancakes' in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly!")

# Allow the player to order again if they like
def order_again():
    response = valid_input("Would you like to order something else? 'yes' or 'no'?\n", "yes", "no")
    
    if 'no' in response:
            print_pause("Okay, goodbye!")
    elif 'yes' in response:
            print_pause("Okay, I'm happy to take another order.")
            get_order()

def order_breakfast():
    intro()
    get_order()    
    order_again()

# Run Game
order_breakfast()
    
    
          