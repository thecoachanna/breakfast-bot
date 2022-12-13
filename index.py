# BREAKFAST BOT GAME

# Get input and use it to determine what happens next
# Handle bad input without crashing
# Be flexible with the input the user can enter
# Print messages to the console, with a short pause after each one
# Allow the player to order again if they like

users_choice = input("Please place your order. Would you like waffles or pancakes?\n")
if users_choice.lower() == 'waffles':
    print("Waffles it is!")
elif users_choice.lower() == 'pancakes':
    print("Pancakes it is!")
else:
    print("Sorry, we don't offer that menu item.")