# ---------------------------------------------------------
# HOMEWORK 3: LOGICAL OPERATORS — and, or, not 🔗
# ---------------------------------------------------------


# TASK 1: Amusement Park Entry
# To ride the roller coaster you must be:
#   - At least 12 years old   AND
#   - At least 140 cm tall
# Ask the user for their age and height.
# Print "Enjoy the ride! 🎢" or "Sorry, you don't meet the requirements."
# Write your code below:




# TASK 2: Free Shipping
# An online shop offers free shipping if:
#   - The order total is >= Rs. 1000  OR
#   - The user is a premium member
# Ask the user for their order total and if they are a premium member (yes/no).
# Print "Free shipping! 🚚" or "Shipping fee: Rs. 100"
# Write your code below:




# TASK 3: Leap Year Checker
# A year is a leap year if:
#   - It is divisible by 4    AND
#   - NOT divisible by 100    OR
#   - Divisible by 400
# Formula: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# Ask for a year and print whether it's a leap year.
# Write your code below:




# ⭐ BONUS CHALLENGE:
# Predict the output of each line BEFORE running — write your guess as a comment.
# Then run the code and check!
a = True
b = False
c = True

print(a and b)          # your guess: ?
print(a or b)           # your guess: ?
print(not b)            # your guess: ?
print(a and b or c)     # your guess: ?
print(not (a or b))     # your guess: ?
print(a and not b and c)# your guess: ?
