import time

# BREAKFAST BOT GAME


# Print messages to the console, with a short pause after each one
print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available:")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)

while True:
    while True:
        # Get input and use it to determine what happens next
        users_choice = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        # Be flexible with the input the user can enter
        if 'waffles' in users_choice:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif 'pancakes' in users_choice:
            print("Pancakes it is!")
            time.sleep(2)
            break
        # Handle bad input without crashing
        else:
            print("Sorry, we don't offer that menu item.")
            time.sleep(2)
    print("Your order will be ready shortly!")
    time.sleep(2)
    # Allow the player to order again if they like
    another_order = input("Would you like to order something else? 'yes' or 'no'?\n").lower()
    while True:
        if 'no' in another_order:
            print("Okay, goodbye!")
            time.sleep(2)
            break
        elif 'yes' in another_order:
            print("Okay, I'm happy to take another order.")
            time.sleep(2)
        else:
            print("I'm sorry, I don't understand.")
    if 'no' in another_order:
        break        