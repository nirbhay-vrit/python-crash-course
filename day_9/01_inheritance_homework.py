# ---------------------------------------------------------
# DAY 9 | HOMEWORK 1: INHERITANCE
# ---------------------------------------------------------
# Instructions:
#   - Read each exercise carefully.
#   - Replace each  pass  or  # TODO  with your solution.
#   - Run the file — there should be no errors.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Write a Vehicle → Car inheritance
# ─────────────────────────────────────────────────────────
# 1. Create a parent class `Vehicle` with:
#    - __init__(self, make, year) setting self.make and self.year
#    - a method start_engine(self) that prints:
#      "<make> engine started."
#
# 2. Create a child class `Car(Vehicle)` with:
#    - __init__(self, make, year, num_doors) — use super()
#    - a method honk(self) that prints:
#      "<make> goes: Beep beep!"
#
# 3. Create a Car object and call all three methods:
#    start_engine(), honk(), and print the year.

class Vehicle:
    pass    # TODO


class Car(Vehicle):
    pass    # TODO


# TODO: create a Car and test all methods


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Method overriding
# ─────────────────────────────────────────────────────────
# Create a class hierarchy:
#   Employee → PartTimeEmployee, FullTimeEmployee
#
# Employee:
#   - __init__(self, name, hourly_rate)
#   - weekly_pay(self) → returns hourly_rate * 40
#
# FullTimeEmployee inherits Employee unchanged (no override).
#
# PartTimeEmployee:
#   - __init__(self, name, hourly_rate, hours_per_week)
#   - weekly_pay(self) → returns hourly_rate * hours_per_week (OVERRIDE)
#
# Test:
#   ft = FullTimeEmployee("Alice", 20)
#   pt = PartTimeEmployee("Bob",   15, 25)
#   print(ft.weekly_pay())   # 800
#   print(pt.weekly_pay())   # 375

class Employee:
    pass    # TODO


class FullTimeEmployee(Employee):
    pass    # TODO


class PartTimeEmployee(Employee):
    pass    # TODO


# TODO: create objects and test


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Using super() to extend __init__
# ─────────────────────────────────────────────────────────
# Create a class `Animal` with __init__(self, name, age)
# and a method info(self) that prints:
#   "Name: <name>, Age: <age>"
#
# Create a class `Dog(Animal)` that adds a `breed` attribute
# and a method profile(self) that prints:
#   "<name> is a <breed>, aged <age>"
#
# Create a Dog object and call both info() and profile().

class Animal:
    pass    # TODO


class Dog(Animal):
    pass    # TODO


# TODO: create a Dog and test


# ─────────────────────────────────────────────────────────
# EXERCISE 4: isinstance() and issubclass()
# ─────────────────────────────────────────────────────────
# Given this hierarchy:
#   LivingThing → Plant, Animal → Dog
#
# Complete the print statements to test isinstance / issubclass.

class LivingThing:
    pass

class Plant(LivingThing):
    pass

class Animal2(LivingThing):
    pass

class Dog2(Animal2):
    pass

fido = Dog2()

# Predict the output BEFORE running, then check:
print(isinstance(fido, Dog2))          # ?
print(isinstance(fido, Animal2))       # ?
print(isinstance(fido, LivingThing))   # ?
print(isinstance(fido, Plant))         # ?

print(issubclass(Dog2, Animal2))       # ?
print(issubclass(Animal2, LivingThing))# ?
print(issubclass(Plant, Animal2))      # ?


# ─────────────────────────────────────────────────────────
# EXERCISE 5 (CHALLENGE): School system
# ─────────────────────────────────────────────────────────
# Build this hierarchy:
#   Person(name, email)
#     └── Student(name, email, student_id, grades=[])
#           • add_grade(score)  — appends to grades
#           • average()        — returns average of grades
#           • status()         — prints pass/fail (avg >= 50)
#     └── Teacher(name, email, subject)
#           • introduce()      — prints "I teach <subject>"
#
# Create one Student and one Teacher.
# Call add_grade() three times on the student.
# Call average(), status(), and introduce().

class Person:
    pass    # TODO


class Student(Person):
    pass    # TODO


class Teacher(Person):
    pass    # TODO


# TODO: create objects and test
