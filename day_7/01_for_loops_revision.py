# ---------------------------------------------------------
# DAY 7 | REVISION 1: FOR LOOPS — Understand It Deeply 🔄
# If the loop confuses you, read EVERY comment here slowly.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS A FOR LOOP? (The big idea)
# ─────────────────────────────────────────────────────────
# A for loop says: "Go through this collection,
# one item at a time, and do something with each item."
#
# You write it ONCE. Python does the repetition for you.
#
# Syntax:
#   for  <variable>  in  <collection>:
#       <do something>
#
# Read it out loud: "FOR each [thing] IN [list], do this."

names = ["Alice", "Bob", "Charlie"]

print("--- Simple loop ---")
for name in names:          # name = Alice, then Bob, then Charlie
    print(name)

# Output:
# Alice
# Bob
# Charlie


# ─────────────────────────────────────────────────────────
# SECTION 2: THE LOOP VARIABLE — What is 'name'?
# ─────────────────────────────────────────────────────────
# 'name' is NOT a special word. You could write anything.
# Python creates it automatically and fills it with the
# CURRENT item from the list each round.
#
# Round 1 →  name = "Alice"
# Round 2 →  name = "Bob"
# Round 3 →  name = "Charlie"
# (loop ends — list is empty)

print("\n--- The loop variable is just a name you choose ---")
for student in names:       # 'student' instead of 'name' — same result!
    print(student)

for x in names:             # even 'x' works — result is the same
    print(x)


# ─────────────────────────────────────────────────────────
# SECTION 3: INDENTATION — The MOST important rule
# ─────────────────────────────────────────────────────────
# ONLY the indented lines repeat.
# Lines that are NOT indented run ONCE after the loop ends.

print("\n--- Indentation matters! ---")
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(f"I found: {fruit}")      # ← INSIDE loop (repeats 3 times)
    print(f"Yum!\n")                # ← INSIDE loop (repeats 3 times)

print("Done looking at fruits.")    # ← OUTSIDE loop (runs once)


# ─────────────────────────────────────────────────────────
# SECTION 4: LOOPING OVER NUMBERS WITH range()
# ─────────────────────────────────────────────────────────
# range(5) gives you the numbers: 0, 1, 2, 3, 4
# range(1, 6) gives you: 1, 2, 3, 4, 5
# range(1, 10, 2) gives you: 1, 3, 5, 7, 9  (step 2)

print("--- range(5): counting from 0 ---")
for i in range(5):
    print(i)         # 0, 1, 2, 3, 4

print("\n--- range(1, 6): counting from 1 ---")
for i in range(1, 6):
    print(i)         # 1, 2, 3, 4, 5

print("\n--- range(1, 10, 2): every other number ---")
for i in range(1, 10, 2):
    print(i)         # 1, 3, 5, 7, 9


# ─────────────────────────────────────────────────────────
# SECTION 5: LOOPING OVER A STRING
# ─────────────────────────────────────────────────────────
# A string is a collection of characters — you can loop through it!

print("\n--- Looping through a string ---")
word = "Python"

for letter in word:
    print(letter)

# P
# y
# t
# h
# o
# n


# ─────────────────────────────────────────────────────────
# SECTION 6: DOING THINGS WITH EACH ITEM
# ─────────────────────────────────────────────────────────
# The real power: you can compute something for EACH item.

print("\n--- Printing scores with a label ---")
scores = [85, 92, 70, 55, 98]

for score in scores:
    if score >= 90:
        print(f"Score {score} → EXCELLENT")
    elif score >= 70:
        print(f"Score {score} → PASS")
    else:
        print(f"Score {score} → FAIL")


# ─────────────────────────────────────────────────────────
# SECTION 7: ACCUMULATOR PATTERN — Building up a result
# ─────────────────────────────────────────────────────────
# Start with a "bucket" (like total = 0).
# Each loop round adds to the bucket.

print("\n--- Sum of scores ---")
total = 0                  # bucket starts empty

for score in scores:
    total = total + score  # add each score to the bucket

print(f"Total: {total}")   # 400
print(f"Average: {total / len(scores)}")  # 80.0


# ─────────────────────────────────────────────────────────
# SECTION 8: LOOP WITH INDEX — enumerate()
# ─────────────────────────────────────────────────────────
# Sometimes you need BOTH the item AND its position number.
# enumerate() gives you: (0, item), (1, item), (2, item)...

print("\n--- Loop with position numbers ---")
students = ["Alice", "Bob", "Charlie", "Diana"]

for index, student in enumerate(students):
    print(f"#{index + 1}: {student}")

# #1: Alice
# #2: Bob
# #3: Charlie
# #4: Diana


# ─────────────────────────────────────────────────────────
# SECTION 9: LOOPING OVER A DICTIONARY
# ─────────────────────────────────────────────────────────
# .items() gives you both the key AND the value.

print("\n--- Looping over a dictionary ---")
ages = {"Alice": 20, "Bob": 25, "Charlie": 22}

for name, age in ages.items():
    print(f"{name} is {age} years old.")
