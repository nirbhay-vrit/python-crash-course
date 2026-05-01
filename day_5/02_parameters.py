# ---------------------------------------------------------
# DAY 5 | TOPIC 2: PARAMETERS — Giving Data to a Function 📬
# Parameters let a function work with DIFFERENT data each call!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE LIMITATION OF A FUNCTION WITH NO INPUT
# ─────────────────────────────────────────────────────────
# Our greet() from Topic 1 always says the SAME thing.
# What if we want to greet DIFFERENT people?

def greet():
    print("Hello, stranger!")

greet()   # Always prints "Hello, stranger!" — not very useful.


# ─────────────────────────────────────────────────────────
# SECTION 2: ADDING A PARAMETER
# ─────────────────────────────────────────────────────────
# Put a variable name inside the () when you DEFINE the function.
# That variable is called a PARAMETER.
# When you CALL the function, you pass a value — called an ARGUMENT.

def greet_person(name):       # 'name' is the PARAMETER
    print(f"Hello, {name}! Welcome to Python class!")

print("\n--- Calling greet_person() with different names ---")
greet_person("Alice")         # "Alice" is the ARGUMENT
greet_person("Bob")
greet_person("Charlie")

# The function runs 3 times, each time with a different name!


# ─────────────────────────────────────────────────────────
# SECTION 3: MULTIPLE PARAMETERS
# ─────────────────────────────────────────────────────────
# You can have as many parameters as you need.
# Separate them with commas inside the ().

def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} called {pet_name}.")

print("\n--- Multiple parameters ---")
describe_pet("Fluffy", "cat")
describe_pet("Rex", "dog")
describe_pet("Nemo", "fish")


# ─────────────────────────────────────────────────────────
# SECTION 4: ORDER MATTERS
# ─────────────────────────────────────────────────────────
# Arguments are matched to parameters LEFT to RIGHT.
# The first argument → first parameter. Second → second. Etc.

def introduce(first_name, age, city):
    print(f"Hi! I'm {first_name}, {age} years old, from {city}.")

print("\n--- Order matters ---")
introduce("Sara", 17, "Kathmandu")
introduce("Tom", 25, "London")

# Watch what happens if you swap the order:
introduce("Kathmandu", "Sara", 17)   # Wrong! Order is off.


# ─────────────────────────────────────────────────────────
# SECTION 5: PARAMETERS WORK JUST LIKE VARIABLES
# ─────────────────────────────────────────────────────────
# Inside the function, a parameter is just a normal variable.
# You can use it in calculations, conditions — anything!

def check_score(score):
    if score >= 60:
        print(f"{score} → PASS ✅")
    else:
        print(f"{score} → FAIL ❌")

print("\n--- Using a parameter in an if statement ---")
check_score(85)
check_score(42)
check_score(60)
