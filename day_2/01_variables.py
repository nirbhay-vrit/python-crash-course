# ---------------------------------------------------------
# DAY 2 | TOPIC 1: VARIABLES 📦
# A variable is like a labeled box that stores information!
# ---------------------------------------------------------


# 1. CREATING YOUR FIRST VARIABLE
# Syntax is simple: variable_name = value
name = "Alice"
age = 15
city = "Kathmandu"

print("Name:", name)
print("Age:", age)
print("City:", city)


# 2. VARIABLES CAN CHANGE!
# You can update the value inside a variable anytime.
print("\n--- Before the birthday ---")
print("Age:", age)

age = 16  # Happy birthday! The box now holds 16.

print("--- After the birthday ---")
print("Age:", age)


# 3. USING VARIABLES IN SENTENCES
# Connect text and variables with the + sign
print("\n--- My Introduction ---")
print("Hi! My name is " + name + " and I am from " + city + ".")


# 4. WHY VARIABLES SAVE THE DAY
# Imagine needing to change a name in 100 places vs just 1!
student = "Bob"
print("\n" + student + " is in the class.")
print(student + " loves Python.")
print(student + " is going to be a great coder!")
# Try changing "Bob" above to another name. Only one change needed!


# 5. NAMING RULES — Very Important!
# ✅ GOOD variable names:
first_name = "Charlie"   # use underscore instead of space
score1 = 100             # numbers are OK (just not at the start)
is_happy = True          # descriptive and clear

# ❌ BAD variable names (uncomment to see the errors!):
# 1score = 100           # ERROR: starts with a number
# my score = 100         # ERROR: has a space
# my-score = 100         # ERROR: has a dash

print("\n--- Naming Examples ---")
print("First name:", first_name)
print("Score:", score1)
print("Is happy:", is_happy)
