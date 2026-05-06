# ---------------------------------------------------------
# DAY 8 | HOMEWORK 1: WHAT IS OOP?
# ---------------------------------------------------------
# Answer each question by writing code below it.
# Run your file after each section to check your output.


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Spot the problem
# ─────────────────────────────────────────────────────────
# Below is messy non-OOP code for tracking books in a library.
# Add a THIRD book (any title, author, pages you like) using the
# same pattern, then print all three books.

book1_title  = "Python Crash Course"
book1_author = "Eric Matthes"
book1_pages  = 544

book2_title  = "Clean Code"
book2_author = "Robert Martin"
book2_pages  = 431

# TODO: Add book3 here (3 variables)

# TODO: Print all three books in the format:
# "Title: ..., Author: ..., Pages: ..."


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Match the vocabulary
# ─────────────────────────────────────────────────────────
# Look at the code below and fill in the blanks in the print statements.

class Car:
    def __init__(self, brand, colour):
        self.brand  = brand
        self.colour = colour

    def honk(self):
        print(f"{self.brand} goes: Beep!")

my_car = Car("Toyota", "red")
my_car.honk()

# TODO: Fill in the blanks — replace ??? with the correct term
#       (class / object / attribute / method)
print("Car is a      : ???")    # Car is a ____
print("my_car is an  : ???")    # my_car is an ____
print("my_car.brand  : ???")    # my_car.brand is an ____
print("my_car.honk() : ???")    # honk is a ____


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Design your own class (on paper first!)
# ─────────────────────────────────────────────────────────
# Think about a "Pizza" in a pizza shop.
# Before writing code, answer:
#   - What ATTRIBUTES would a Pizza have?  (data it knows)
#   - What METHODS would a Pizza have?     (things it can do)
#
# Write your answers as comments below, then write a very simple
# class (just the class line and pass for now — no __init__ yet):

# Attributes a Pizza might have:
# 1. ???
# 2. ???
# 3. ???

# Methods a Pizza might have:
# 1. ???
# 2. ???

# TODO: Write the class skeleton here (class Pizza: ... pass)


# ─────────────────────────────────────────────────────────
# EXERCISE 4: True or False?
# ─────────────────────────────────────────────────────────
# Write True or False for each statement as a comment.

# a) A class is like a blueprint, and objects are things built from it.  → ???
# b) You can only create ONE object from a class.                         → ???
# c) Attributes store data; methods define behaviour.                     → ???
# d) OOP helps keep related data bundled together.                        → ???
# e) You must write a new class every time you need a new object.         → ???
