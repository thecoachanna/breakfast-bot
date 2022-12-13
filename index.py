# BREAKFAST BOT GAME


# Print messages to the console, with a short pause after each one
# Allow the player to order again if they like

while True:
    # Get input and use it to determine what happens next
    users_choice = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    # Be flexible with the input the user can enter
    if 'waffles' in users_choice:
        print("Waffles it is!")
        break
    elif 'pancakes' in users_choice:
        print("Pancakes it is!")
        break
    # Handle bad input without crashing
    else:
        print("Sorry, we don't offer that menu item.")