# ---------------------------------------------------------
# DAY 8 | TOPIC 1: WHAT IS OBJECT-ORIENTED PROGRAMMING?
# Understanding WHY OOP exists before learning HOW to use it.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM — Code Without OOP
# ─────────────────────────────────────────────────────────
# Imagine you are building a student management system.
# Without OOP, you track each student using separate variables:

student1_name  = "Alice"
student1_age   = 20
student1_grade = "A"

student2_name  = "Bob"
student2_age   = 22
student2_grade = "B"

student3_name  = "Charlie"
student3_age   = 21
student3_grade = "C"

print("--- Students (without OOP) ---")
print(f"{student1_name}, Age: {student1_age}, Grade: {student1_grade}")
print(f"{student2_name}, Age: {student2_age}, Grade: {student2_grade}")
print(f"{student3_name}, Age: {student3_age}, Grade: {student3_grade}")

# What is wrong with this approach?
#   ❌ Adding a 4th student means 3 MORE variables
#   ❌ Easy to mix up: student1_age vs student2_age
#   ❌ 100 students = 300 variables — impossible to manage!
#   ❌ The data for one student is scattered across 3 separate variables


# ─────────────────────────────────────────────────────────
# SECTION 2: TRYING TO FIX IT WITH LISTS
# ─────────────────────────────────────────────────────────
# Some people try parallel lists — slightly better, but still bad:

names  = ["Alice",  "Bob",  "Charlie"]
ages   = [20,       22,     21]
grades = ["A",      "B",    "C"]

print("\n--- Students (parallel lists) ---")
for i in range(len(names)):
    print(f"{names[i]}, Age: {ages[i]}, Grade: {grades[i]}")

# Still wrong:
#   ❌ What if someone inserts into 'names' but forgets 'ages'?
#   ❌ The connection between one student's name/age/grade is fragile.
#   ❌ To "add a student" you must touch 3 separate lists.


# ─────────────────────────────────────────────────────────
# SECTION 3: WHAT IS OOP? — The Big Idea
# ─────────────────────────────────────────────────────────
# OOP = Object-Oriented Programming
#
# The core idea is simple:
#   Instead of tracking data in separate variables,
#   BUNDLE the related data AND behaviour together into one unit.
#
# That unit is called an OBJECT.
#
# An object holds:
#   ATTRIBUTES (data)    → what it KNOWS    (name, age, grade)
#   METHODS (functions)  → what it CAN DO   (study, get_report)
#
# To create objects, you first define a CLASS — a blueprint.
#
#   CLASS  = blueprint / template    (the cookie cutter)
#   OBJECT = a real thing from the blueprint (the actual cookie)
#
# You define the class ONCE. Then create as many objects as you need.


# ─────────────────────────────────────────────────────────
# SECTION 4: A FIRST LOOK — Sneak Peek at OOP
# ─────────────────────────────────────────────────────────
# Don't worry about every detail yet. Just READ what it does.

class Student:
    def __init__(self, name, age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def introduce(self):
        print(f"Hi! I'm {self.name}, age {self.age}, grade: {self.grade}")

# Create objects from the blueprint:
s1 = Student("Alice",   20, "A")
s2 = Student("Bob",     22, "B")
s3 = Student("Charlie", 21, "C")

print("\n--- Students (with OOP) ---")
s1.introduce()
s2.introduce()
s3.introduce()

# What changed?
#   ✅ Each student is its OWN object — data bundled together.
#   ✅ Adding a 4th student: s4 = Student("Diana", 19, "A") — ONE line.
#   ✅ No chance of mixing up Alice's grade with Bob's grade.
#   ✅ The 'introduce' method lives WITH the data, not floating around.


# ─────────────────────────────────────────────────────────
# SECTION 5: OOP VOCABULARY — The 4 Key Words
# ─────────────────────────────────────────────────────────
# These are words you will see everywhere in OOP:
#
#   CLASS      — the blueprint / template
#   OBJECT     — a real instance created from the class
#   ATTRIBUTE  — data stored inside an object   (self.name)
#   METHOD     — a function that belongs to the class  (introduce)
#
# Real-world example:
#   "Dog"       is a CLASS.
#   My dog "Rex" is an OBJECT (also called an INSTANCE).
#   Rex's colour, weight, breed → ATTRIBUTES.
#   rex.bark(), rex.sit(), rex.eat() → METHODS.

print("\n--- OOP vocabulary in action ---")
print(f"Class     → Student  (the blueprint)")
print(f"Object    → s1, s2, s3  (real student objects)")
print(f"Attribute → s1.name is '{s1.name}'")
print(f"Method    → s1.introduce() prints the student's info")
