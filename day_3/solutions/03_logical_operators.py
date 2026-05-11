# ---------------------------------------------------------
# SOLUTION 3: LOGICAL OPERATORS — and, or, not 🔗
# ---------------------------------------------------------
# `and` → True only if BOTH sides are True
# `or`  → True if EITHER side is True
# `not` → flips True ↔ False


# TASK 1: Amusement Park Entry.
age = int(input("Your age: "))
height = int(input("Your height (cm): "))
if age >= 12 and height >= 140:
    print("Enjoy the ride! 🎢")
else:
    print("Sorry, you don't meet the requirements.")


# TASK 2: Free Shipping.
total = float(input("Order total (Rs): "))
premium_input = input("Premium member? (yes/no): ").lower()
is_premium = (premium_input == "yes")
if total >= 1000 or is_premium:
    print("Free shipping! 🚚")
else:
    print("Shipping fee: Rs. 100")


# TASK 3: Leap Year Checker.
# Standard rule: divisible by 4 AND not by 100 — UNLESS also divisible by 400.
year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is NOT a leap year.")


# ⭐ BONUS CHALLENGE: predicting outputs.
a = True
b = False
c = True

print(a and b)              # False   (b is False, so AND is False)
print(a or b)               # True    (a is True, so OR is True)
print(not b)                # True    (flip of False is True)
print(a and b or c)         # True    → (True and False) or True → False or True
print(not (a or b))         # False   → not(True) → False
print(a and not b and c)    # True    → True and True and True
