# ---------------------------------------------------------
# DAY 8 | HOMEWORK 2: CLASSES AND OBJECTS
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Your first class
# ─────────────────────────────────────────────────────────
# Define a class called 'Phone' (just use 'pass' in the body).
# Then create THREE Phone objects: phone1, phone2, phone3.
# Give each phone these attributes manually (dot notation):
#   .brand  (e.g. "Samsung", "Apple", "OnePlus")
#   .colour (e.g. "black", "white", "blue")
#   .price  (e.g. 30000, 80000, 25000)
# Print all three phones in the format:
#   "Brand: ..., Colour: ..., Price: ..."

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 2: type() and isinstance()
# ─────────────────────────────────────────────────────────
# Given this class and these objects, predict what each
# print() will output. Write your prediction as a comment,
# THEN run the code and check if you were right.

class Laptop:
    pass

lp1 = Laptop()
lp2 = Laptop()

lp1.brand = "Dell"
lp2.brand = "HP"

# Predict the output of each line below (write as comment):
print(type(lp1))          # → ???
print(type(lp2))          # → ???
print(isinstance(lp1, Laptop))   # → ???
print(isinstance(42, Laptop))    # → ???
print(lp1 == lp2)         # → ???
print(lp1 is lp2)         # → ???


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Create and modify
# ─────────────────────────────────────────────────────────
# 1. Define a class called 'Superhero'
# 2. Create a superhero named 'Batman' with:
#       .name  = "Batman"
#       .power = "Gadgets"
#       .city  = "Gotham"
# 3. Print the hero's details.
# 4. Change the city to "Metropolis" and print again.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Mini inventory
# ─────────────────────────────────────────────────────────
# Define a class called 'FruitItem'.
# Create 4 fruit objects (apple, banana, mango, grape).
# Give each: .name, .price_per_kg, .stock_kg
# Store all 4 in a list called 'inventory'.
# Loop through the list and print each fruit's details.

# TODO: Write your code here
