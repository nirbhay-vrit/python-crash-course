# ---------------------------------------------------------
# DAY 8 | TOPIC 2: CLASSES AND OBJECTS
# How to define a class and create objects from it.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: DEFINING A CLASS
# ─────────────────────────────────────────────────────────
# Syntax:
#
#   class ClassName:
#       [indented body]
#
# Rules:
#   - 'class' is a keyword (like 'def' for functions)
#   - ClassName uses CapWords / PascalCase: each word capitalised
#       ✅  Dog, BankAccount, StudentRecord
#       ❌  dog, bank_account, studentrecord
#   - The body is indented (just like a function body)
#
# The simplest possible class — it does nothing yet:

class Dog:
    pass    # 'pass' means: body is intentionally empty

print("Dog class defined successfully!")
print(Dog)          # <class '__main__.Dog'>


# ─────────────────────────────────────────────────────────
# SECTION 2: CREATING OBJECTS (INSTANCES)
# ─────────────────────────────────────────────────────────
# Once a class exists, create objects from it like this:
#
#   variable_name = ClassName()
#
# This is called INSTANTIATION — you are creating an INSTANCE.
# The words "object" and "instance" mean the same thing.

rex   = Dog()   # rex   is one Dog instance
buddy = Dog()   # buddy is another Dog instance
fido  = Dog()   # fido  is a third Dog instance

print("\n--- Three dog objects ---")
print(rex)    # <__main__.Dog object at 0x...> — shows memory address
print(buddy)
print(fido)

# Are rex and buddy the same object?
print("\n--- Are they the same? ---")
print(rex == buddy)   # False — different objects even with same class
print(rex is buddy)   # False — 'is' checks if same spot in memory


# ─────────────────────────────────────────────────────────
# SECTION 3: GIVING OBJECTS ATTRIBUTES MANUALLY
# ─────────────────────────────────────────────────────────
# You can attach data to an object after creation using dot notation:
#   object.attribute_name = value

rex.name  = "Rex"
rex.breed = "Labrador"
rex.age   = 3

buddy.name  = "Buddy"
buddy.breed = "Poodle"
buddy.age   = 5

print("\n--- Dog attributes via dot notation ---")
print(f"Name: {rex.name},   Breed: {rex.breed},  Age: {rex.age}")
print(f"Name: {buddy.name}, Breed: {buddy.breed}, Age: {buddy.age}")

# This works, BUT it is fragile:
#   ❌ What if you forget to set rex.age?
#   ❌ What if someone sets rex.naem by typo?
# That is exactly what __init__ solves — coming next topic!


# ─────────────────────────────────────────────────────────
# SECTION 4: READING AND USING ATTRIBUTES
# ─────────────────────────────────────────────────────────
# Read any attribute using:   object.attribute

print("\n--- Reading attributes ---")
print(rex.name)    # Rex
print(rex.age)     # 3

# Use them in expressions:
print(f"{rex.name} will be {rex.age + 1} years old next year.")

# Change an attribute:
rex.age = 4
print(f"After birthday: {rex.name} is now {rex.age}.")


# ─────────────────────────────────────────────────────────
# SECTION 5: type() AND isinstance() — Checking Object Identity
# ─────────────────────────────────────────────────────────
# type(x) tells you the CLASS of any object.

print("\n--- type() checks ---")
print(type(rex))         # <class '__main__.Dog'>
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>

# 💡 Everything in Python is an object!
#    int, str, list — all are classes.
#    When you write "hello" you are creating a str object.

# isinstance(x, ClassName) → True or False
print("\n--- isinstance() checks ---")
print(isinstance(rex, Dog))    # True  — rex IS a Dog
print(isinstance(42,  int))    # True  — 42  IS an int
print(isinstance(rex, int))    # False — rex is NOT an int


# ─────────────────────────────────────────────────────────
# SECTION 6: MANY OBJECTS FROM ONE CLASS
# ─────────────────────────────────────────────────────────
# The class is defined ONCE. You can create unlimited objects.
# Each object is independent — changing one does NOT affect others.

class Car:
    pass

car1 = Car()
car2 = Car()
car3 = Car()

car1.brand = "Toyota"
car2.brand = "Honda"
car3.brand = "BMW"

car1.speed = 0
car2.speed = 60
car3.speed = 120

print("\n--- Many cars from one class ---")
for car in [car1, car2, car3]:
    print(f"  {car.brand} going at {car.speed} km/h")

# One class → unlimited objects. That is the power of OOP.
