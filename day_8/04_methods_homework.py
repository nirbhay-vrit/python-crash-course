# ---------------------------------------------------------
# DAY 8 | HOMEWORK 4: METHODS
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Add methods to a class
# ─────────────────────────────────────────────────────────
# Below is a class with only __init__. Add two methods:
#
#   full_name(self)  → returns "FirstName LastName" as a string
#   greet(self)      → prints "Hello, my name is FirstName LastName!"
#
# Then create 2 Person objects and call both methods on each.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    # TODO: def full_name(self): ...
    # TODO: def greet(self): ...

# TODO: Create two Person objects and test your methods


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Method that modifies an attribute
# ─────────────────────────────────────────────────────────
# Complete the 'TrafficLight' class by implementing:
#
#   next_light(self)  → changes the colour in order:
#                        red → green → yellow → red → ...
#                        Print the new colour each time.
#   show(self)        → prints "Current light: <colour>"

class TrafficLight:
    def __init__(self):
        self.colour = "red"

    def show(self):
        print(f"Current light: {self.colour}")

    def next_light(self):
        # TODO: change self.colour to the next in sequence
        # red → green → yellow → red → ...
        pass

# Test it:
light = TrafficLight()
light.show()       # Current light: red
light.next_light() # green
light.next_light() # yellow
light.next_light() # red
light.next_light() # green


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Method returning a value
# ─────────────────────────────────────────────────────────
# Create a class 'ShoppingCart' with:
#   __init__(self)         → self.items = []  (empty list)
#   add_item(self, name, price)  → add {"name": name, "price": price} to self.items
#   total(self)            → returns the sum of all item prices
#   receipt(self)          → prints each item and its price, then the total
#
# Test:
#   cart = ShoppingCart()
#   cart.add_item("Apple",  20)
#   cart.add_item("Bread",  35)
#   cart.add_item("Milk",   25)
#   cart.receipt()   # should print all items + total of 80

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Methods calling methods
# ─────────────────────────────────────────────────────────
# Create a 'Rectangle' class with:
#   __init__(self, width, height)
#   area(self)         → returns width * height
#   perimeter(self)    → returns 2 * (width + height)
#   is_square(self)    → returns True if width == height
#   describe(self)     → prints all 3 pieces of info, calling the above methods
#
# Create rectangles 4×6, 5×5, 10×3 and call describe() on each.

# TODO: Write your code here
