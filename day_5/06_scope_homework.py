# ---------------------------------------------------------
# HOMEWORK 6: SCOPE 🌍
# ---------------------------------------------------------


# TASK 1: Local vs Global
# What will this print? Predict first, then run to check:

secret = "global secret"

def mystery():
    secret = "local secret"
    print(secret)

print(secret)      # Prediction: __________
mystery()          # Prediction: __________
print(secret)      # Prediction: __________

# Write your predictions as comments, then uncomment the lines to check!


# TASK 2: Fix the Bug
# This code has a bug! Can you spot it and fix it?

count = 0

def increment():
    count += 1      # BUG: can't modify global without 'global' keyword!
    print(count)

# Uncomment to test (after you fix it):
# increment()
# increment()


# TASK 3: Better Counter
# Rewrite the increment function from TASK 2 WITHOUT using 'global'.
# Instead, use a parameter and return value.
# Write your code below:





# TASK 4: Calculator with Constants
# Create these constants at the top:
#   TAX_RATE = 0.08
#   SHIPPING_COST = 5.0
# Define a function called 'calculate_total' that takes 'subtotal'
# and returns: subtotal + (subtotal * TAX_RATE) + SHIPPING_COST
# Test it with subtotals of 50 and 100.
# Write your code below:





# TASK 5: Shadowing Challenge
# Given this global variable:
score = 100

# Define a function called 'play_game' that:
#   - Creates a local variable also called 'score' with value 50
#   - Prints the local score
#   - Returns the local score
# Call the function and store the result in a variable.
# Print the global score after the function call.
# Write your code below:





# ⭐ BONUS CHALLENGE:
# Define a function called 'create_counter' that uses 'nonlocal'
# (look it up!) or nested functions to create a counter that
# remembers its value between calls WITHOUT using global.
# Hint: You'll need to define a function inside another function.
# Write your code below:

