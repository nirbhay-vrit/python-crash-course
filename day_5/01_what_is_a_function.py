# ---------------------------------------------------------
# DAY 5 | TOPIC 1: WHAT IS A FUNCTION? 🧩
# A function is a reusable block of code you name and call!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM FUNCTIONS SOLVE
# ─────────────────────────────────────────────────────────
# Imagine you want to greet someone three times in your program.
# WITHOUT a function, you repeat the same code over and over:

print("Hello! Welcome to Python class.")
print("We are happy you are here.")
print("Let's learn something great today!")

print("---")

print("Hello! Welcome to Python class.")
print("We are happy you are here.")
print("Let's learn something great today!")

print("---")

print("Hello! Welcome to Python class.")
print("We are happy you are here.")
print("Let's learn something great today!")

# That's 9 lines for the same 3 lines repeated 3 times.
# What if you need to change one word? You change it 3 times!
# Functions solve this by letting you write the code ONCE.


# ─────────────────────────────────────────────────────────
# SECTION 2: DEFINING YOUR FIRST FUNCTION
# ─────────────────────────────────────────────────────────
# Use the 'def' keyword, then give it a name, then add ()
# The body (what it does) must be INDENTED.

def greet():
    print("Hello! Welcome to Python class.")
    print("We are happy you are here.")
    print("Let's learn something great today!")

# Notice: defining the function does NOT run it yet.
# Nothing printed yet! The function is just "saved".


# ─────────────────────────────────────────────────────────
# SECTION 3: CALLING A FUNCTION
# ─────────────────────────────────────────────────────────
# To RUN the function, you "call" it by writing its name
# followed by parentheses ().

print("\n--- Calling greet() three times ---")
greet()
print("---")
greet()
print("---")
greet()

# Now the 9 lines above are replaced with just 3 calls!
# And if you need to change the greeting, you only edit ONE place.


# ─────────────────────────────────────────────────────────
# SECTION 4: ANATOMY OF A FUNCTION
# ─────────────────────────────────────────────────────────
#
#   def  say_hello():
#   ↑         ↑    ↑↑
#   keyword  name  ()  ← parentheses always required
#       print("Hi!")   ← body, indented 4 spaces
#
# To call it:
#   say_hello()        ← name + () again
#

def say_hello():
    print("Hi from say_hello()!")

print("\n--- Calling say_hello() ---")
say_hello()


# ─────────────────────────────────────────────────────────
# SECTION 5: FUNCTIONS CAN HOLD ANY CODE
# ─────────────────────────────────────────────────────────
# The function body can contain variables, calculations,
# loops — anything you've already learned!

def print_five_stars():
    for i in range(5):
        print("⭐" * (i + 1))

print("\n--- Calling print_five_stars() ---")
print_five_stars()
