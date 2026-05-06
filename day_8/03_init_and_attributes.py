# ---------------------------------------------------------
# DAY 8 | TOPIC 3: __init__ AND ATTRIBUTES
# __init__ is called automatically when you create an object.
# It is the CONSTRUCTOR — it sets up the object's starting state.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM WITHOUT __init__
# ─────────────────────────────────────────────────────────
# Without __init__, you set attributes manually after creation.
# This is risky — you might forget one or make a typo.

class DogBad:
    pass

d = DogBad()
d.name = "Rex"
# We forgot to set d.age!
# Any code that uses d.age will CRASH:
# print(d.age)   # AttributeError: 'DogBad' object has no attribute 'age'

print("Without __init__: must set every attribute manually. Risky!")


# ─────────────────────────────────────────────────────────
# SECTION 2: __init__ — THE CONSTRUCTOR
# ─────────────────────────────────────────────────────────
# __init__ is a SPECIAL METHOD (note the double underscores).
# Python calls it AUTOMATICALLY the moment you create a new object.
# You use it to set up all the attributes in one safe place.
#
# Syntax:
#
#   class Dog:
#       def __init__(self, name, age):    ← Python calls this for you
#           self.name = name              ← attach data to the object
#           self.age  = age
#
# When you write:   rex = Dog("Rex", 3)
# Python internally does:  Dog.__init__(rex, "Rex", 3)
#
# You NEVER call __init__ yourself — Python does it automatically.

class Dog:
    def __init__(self, name, age):
        self.name = name    # store name ON this object
        self.age  = age     # store age  ON this object

# Creating objects — __init__ is called instantly:
rex   = Dog("Rex",   3)    # name="Rex", age=3
buddy = Dog("Buddy", 5)    # name="Buddy", age=5

print("\n--- __init__ in action ---")
print(f"rex.name   = {rex.name}")     # Rex
print(f"rex.age    = {rex.age}")      # 3
print(f"buddy.name = {buddy.name}")   # Buddy
print(f"buddy.age  = {buddy.age}")    # 5


# ─────────────────────────────────────────────────────────
# SECTION 3: UNDERSTANDING `self`
# ─────────────────────────────────────────────────────────
# `self` is ALWAYS the first parameter of __init__ (and all methods).
# `self` refers to THE SPECIFIC OBJECT being created right now.
#
# When you write:   rex = Dog("Rex", 3)
# Python passes rex as `self` automatically.
#
# Inside __init__:
#   self.name = name
# means:
#   "On THIS specific dog object, store a name attribute."
#
# self.name  → stored ON the object permanently
# name       → just a local variable, gone when __init__ finishes
#
# Think of self as "me":
#   self.name = "Rex"  →  "My name is Rex"
#   self.age  = 3      →  "My age is 3"

class Cat:
    def __init__(self, name, colour):
        # self = the specific Cat being created right now
        self.name   = name     # permanently stored on this Cat
        self.colour = colour   # permanently stored on this Cat
        # 'name' and 'colour' without self only exist during __init__

whiskers = Cat("Whiskers", "grey")
luna     = Cat("Luna",     "white")

print("\n--- self in action ---")
print(f"whiskers → name: {whiskers.name}, colour: {whiskers.colour}")
print(f"luna     → name: {luna.name},     colour: {luna.colour}")

# Each object has its OWN copy of every attribute:
print(f"\nwhiskers.name = '{whiskers.name}'  ← whiskers' own name")
print(f"luna.name     = '{luna.name}'       ← luna's own name")
# Changing one does NOT affect the other:
whiskers.colour = "black"
print(f"\nAfter change: whiskers={whiskers.colour}, luna={luna.colour}")


# ─────────────────────────────────────────────────────────
# SECTION 4: STEP-BY-STEP — What Happens When You Create an Object
# ─────────────────────────────────────────────────────────
# Let's trace:  rex = Dog("Rex", 3)
#
#   Step 1: Python creates a new empty Dog object in memory.
#   Step 2: Python calls __init__(that_new_object, "Rex", 3)
#           → self = the new object, name = "Rex", age = 3
#   Step 3: self.name = "Rex"  → stored on the object
#   Step 4: self.age  = 3      → stored on the object
#   Step 5: __init__ finishes.
#   Step 6: Python returns the finished object and assigns it to rex.
#
# After that, rex.name is "Rex" and rex.age is 3 — forever (until changed).


# ─────────────────────────────────────────────────────────
# SECTION 5: DEFAULT VALUES IN __init__
# ─────────────────────────────────────────────────────────
# __init__ can have default parameter values — just like regular functions.

class Player:
    def __init__(self, name, score=0, level=1):
        self.name  = name
        self.score = score   # default 0 if not provided
        self.level = level   # default 1 if not provided

p1 = Player("Alice")                     # score=0,   level=1
p2 = Player("Bob",   score=500)          # score=500, level=1
p3 = Player("Charlie", score=200, level=3)  # score=200, level=3

print("\n--- Default values in __init__ ---")
print(f"{p1.name}: score={p1.score}, level={p1.level}")
print(f"{p2.name}: score={p2.score}, level={p2.level}")
print(f"{p3.name}: score={p3.score}, level={p3.level}")


# ─────────────────────────────────────────────────────────
# SECTION 6: MODIFYING ATTRIBUTES AFTER CREATION
# ─────────────────────────────────────────────────────────
# You can always change an attribute using dot notation.

print("\n--- Modifying attributes ---")
p1.score = 150       # Alice earned points
p1.level = 2         # Alice levelled up
print(f"{p1.name}: score={p1.score}, level={p1.level}")

p2.score += 50       # add 50 to Bob's existing score
print(f"{p2.name}: score={p2.score}")


# ─────────────────────────────────────────────────────────
# SECTION 7: COMPUTED ATTRIBUTES IN __init__
# ─────────────────────────────────────────────────────────
# __init__ can compute attributes from the input — not just store them.

class Rectangle:
    def __init__(self, width, height):
        self.width     = width
        self.height    = height
        self.area      = width * height          # computed from input
        self.perimeter = 2 * (width + height)    # computed from input

r1 = Rectangle(5, 3)
r2 = Rectangle(10, 4)

print("\n--- Computed attributes ---")
print(f"Rectangle 5×3:   area={r1.area}, perimeter={r1.perimeter}")
print(f"Rectangle 10×4:  area={r2.area}, perimeter={r2.perimeter}")
