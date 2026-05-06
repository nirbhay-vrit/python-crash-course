# ---------------------------------------------------------
# DAY 8 | HOMEWORK 3: __init__ AND ATTRIBUTES
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Your first __init__
# ─────────────────────────────────────────────────────────
# Create a class called 'Book' with __init__ that takes:
#   title, author, pages
# Store all three as attributes using self.
# Create 3 Book objects and print each in this format:
#   "'Clean Code' by Robert Martin — 431 pages"

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Default values
# ─────────────────────────────────────────────────────────
# Create a class 'Employee' with:
#   __init__(self, name, department, salary=30000)
# Create:
#   emp1 = Employee("Alice", "Engineering")         # salary uses default
#   emp2 = Employee("Bob",   "Sales",      45000)   # salary overridden
#   emp3 = Employee("Carol", "HR",         38000)   # salary overridden
# Print each employee's details.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Computed attributes
# ─────────────────────────────────────────────────────────
# Create a class 'Circle' with:
#   __init__(self, radius)
#   Compute and store:
#       self.area         = 3.14159 * radius * radius
#       self.circumference = 2 * 3.14159 * radius
# Create circles with radius 5, 10, 15 and print all values.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Understand self
# ─────────────────────────────────────────────────────────
# Look at this code. What will it print? Write your predictions
# as comments, THEN run it to verify.

class Counter:
    def __init__(self, start=0):
        self.value = start

c1 = Counter()        # no argument
c2 = Counter(10)      # start at 10
c3 = Counter(100)     # start at 100

c1.value += 5
c2.value += 5

print(c1.value)   # → ???
print(c2.value)   # → ???
print(c3.value)   # → ???


# ─────────────────────────────────────────────────────────
# EXERCISE 5: Mini challenge — Temperature class
# ─────────────────────────────────────────────────────────
# Create a class 'Temperature' with:
#   __init__(self, celsius)
#   Compute and store:
#       self.fahrenheit = (celsius * 9/5) + 32
#       self.kelvin     = celsius + 273.15
# Create objects for 0°C, 100°C, and -40°C.
# Print all values for each object.

# TODO: Write your code here
