# ---------------------------------------------------------
# DAY 6 | TOPIC 2: *args — Variable Positional Arguments ✳️
# What if you don't know how many arguments you'll get?
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM — UNKNOWN NUMBER OF ARGUMENTS
# ─────────────────────────────────────────────────────────
# Imagine writing a function to add numbers.
# How many numbers will the caller pass? 2? 5? 100?

def add_two(a, b):
    return a + b

def add_three(a, b, c):
    return a + b + c

# This approach doesn't scale. What if someone passes 10 numbers?
# We need a better way!


# ─────────────────────────────────────────────────────────
# SECTION 2: INTRODUCING *args
# ─────────────────────────────────────────────────────────
# The *args syntax collects ALL extra positional arguments
# into a TUPLE that you can loop over or use like any tuple.
# The name 'args' is a convention — the * is what matters.

def add_all(*args):
    total = 0
    for number in args:
        total += number
    return total

print("--- *args in action ---")
print(add_all(1, 2))               # 3
print(add_all(1, 2, 3))            # 6
print(add_all(10, 20, 30, 40, 50)) # 150
print(add_all())                   # 0  (works with zero args too!)


# ─────────────────────────────────────────────────────────
# SECTION 3: WHAT IS *args EXACTLY?
# ─────────────────────────────────────────────────────────
# Inside the function, args is a TUPLE of everything passed.
# You can loop over it, index it, check its length, etc.

def inspect_args(*args):
    print(f"Type:   {type(args)}")
    print(f"Values: {args}")
    print(f"Count:  {len(args)}")

print("\n--- Inspecting *args ---")
inspect_args("apple", "banana", "cherry")
# Type:   <class 'tuple'>
# Values: ('apple', 'banana', 'cherry')
# Count:  3


# ─────────────────────────────────────────────────────────
# SECTION 4: *args WITH REGULAR PARAMETERS
# ─────────────────────────────────────────────────────────
# You can have regular parameters BEFORE *args.
# Regular params come first, then *args catches everything else.

def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

print("\n--- Regular params + *args ---")
greet_all("Hello", "Alice", "Bob", "Charlie")
greet_all("Hey", "Zoe")
# 'greeting' gets "Hello", *names gets ("Alice", "Bob", "Charlie")


# ─────────────────────────────────────────────────────────
# SECTION 5: BUILDING A FLEXIBLE CALCULATOR
# ─────────────────────────────────────────────────────────
# Let's build a calculator that can add, multiply, or find
# the average of ANY number of values.

def calculate(operation, *numbers):
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for n in numbers:
            result *= n
        return result
    elif operation == "average":
        return sum(numbers) / len(numbers)
    else:
        return "Unknown operation"

print("\n--- Flexible calculator ---")
print(calculate("add", 1, 2, 3, 4, 5))         # 15
print(calculate("multiply", 2, 3, 4))           # 24
print(calculate("average", 10, 20, 30, 40))     # 25.0


# ─────────────────────────────────────────────────────────
# SECTION 6: UNPACKING A LIST INTO A FUNCTION WITH *
# ─────────────────────────────────────────────────────────
# You can also PASS a list to a function using * to unpack it.
# This is the flip side of collecting with *args.

def add_three_numbers(a, b, c):
    return a + b + c

nums = [10, 20, 30]

print("\n--- Unpacking a list with * ---")
print(add_three_numbers(*nums))    # same as add_three_numbers(10, 20, 30)
# Output: 60
