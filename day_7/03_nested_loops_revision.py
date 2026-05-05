# ---------------------------------------------------------
# DAY 7 | REVISION 3: NESTED LOOPS — Loop Inside a Loop 🔲
# A nested loop is simply one loop living INSIDE another.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS A NESTED LOOP?
# ─────────────────────────────────────────────────────────
# Think of a clock:
#   - The HOUR hand goes around 12 times a day   (outer loop)
#   - For EVERY hour, the MINUTE hand goes around 60 times (inner loop)
#
# For every 1 step of the outer loop,
# the inner loop completes ALL of its steps.
#
# Structure:
#   for outer_item in outer_collection:       ← outer loop
#       for inner_item in inner_collection:   ← inner loop
#           print(outer_item, inner_item)     ← runs for EVERY combo


# ─────────────────────────────────────────────────────────
# SECTION 2: SIMPLEST EXAMPLE — Pairs
# ─────────────────────────────────────────────────────────
# Let's print every combination of colour + size.

print("--- Every colour + size combo ---")
colours = ["Red", "Blue"]
sizes   = ["Small", "Large"]

for colour in colours:              # outer: runs 2 times
    for size in sizes:              # inner: runs 2 times FOR EACH colour
        print(f"{colour} {size}")

# Output:
# Red Small
# Red Large
# Blue Small
# Blue Large
#
# How many lines? 2 colours × 2 sizes = 4 lines total


# ─────────────────────────────────────────────────────────
# SECTION 3: TRACE THROUGH STEP BY STEP
# ─────────────────────────────────────────────────────────
# Let's use numbers so we can see EXACTLY what happens.

print("\n--- Step-by-step trace with i and j ---")
for i in range(1, 4):           # i goes: 1, 2, 3
    for j in range(1, 4):       # j goes: 1, 2, 3 for EACH i
        print(f"  i={i}, j={j}")
    print(f"--- finished inner loop for i={i} ---")

# i=1 → j runs as 1, 2, 3
# i=2 → j runs as 1, 2, 3
# i=3 → j runs as 1, 2, 3
# Total prints of i,j: 3 × 3 = 9


# ─────────────────────────────────────────────────────────
# SECTION 4: PRACTICAL EXAMPLE 1 — Multiplication Table
# ─────────────────────────────────────────────────────────
# Classic use-case for nested loops.

print("\n--- Multiplication table (1-5) ---")
for row in range(1, 6):
    for col in range(1, 6):
        product = row * col
        print(f"{product:4}", end="")    # end="" keeps it on same line
    print()                              # new line after each row

# Output (formatted):
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25


# ─────────────────────────────────────────────────────────
# SECTION 5: PRACTICAL EXAMPLE 2 — Grid of Stars
# ─────────────────────────────────────────────────────────
# Nested loops are great for printing patterns and grids.

print("\n--- 4×6 grid of stars ---")
rows = 4
cols = 6

for r in range(rows):
    for c in range(cols):
        print("*", end=" ")     # print on same line
    print()                     # go to next line after each row

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *


# ─────────────────────────────────────────────────────────
# SECTION 6: STAIRCASE PATTERN — Inner loop depends on outer
# ─────────────────────────────────────────────────────────
# The cool part: the inner loop can use the outer loop variable!

print("\n--- Staircase ---")
for row in range(1, 6):           # row goes 1, 2, 3, 4, 5
    for col in range(row):        # col goes 0..row-1 (so 'row' stars)
        print("#", end="")
    print()

# Output:
# #
# ##
# ###
# ####
# #####


# ─────────────────────────────────────────────────────────
# SECTION 7: PRACTICAL EXAMPLE 3 — Students and Scores
# ─────────────────────────────────────────────────────────
# A real scenario: loop over students, and for each student
# loop over their scores.

print("\n--- Student score report ---")
class_data = [
    {"name": "Alice",   "scores": [85, 90, 78]},
    {"name": "Bob",     "scores": [60, 72, 65]},
    {"name": "Charlie", "scores": [95, 88, 92]},
]

for student in class_data:             # outer: each student
    name = student["name"]
    print(f"\n{name}'s scores:")
    total = 0
    for score in student["scores"]:    # inner: each score
        print(f"  - {score}")
        total += score
    average = total / len(student["scores"])
    print(f"  Average: {average:.1f}")


# ─────────────────────────────────────────────────────────
# SECTION 8: break INSIDE NESTED LOOPS
# ─────────────────────────────────────────────────────────
# IMPORTANT: break only exits the INNER loop, not the outer one!

print("\n--- break only exits the INNER loop ---")
for i in range(1, 4):
    print(f"Outer i = {i}")
    for j in range(1, 6):
        if j == 3:
            print(f"  Breaking inner at j={j}")
            break            # exits inner loop, outer keeps going
        print(f"  Inner j = {j}")

# Outer i=1: inner prints j=1, j=2, then breaks
# Outer i=2: inner prints j=1, j=2, then breaks
# Outer i=3: inner prints j=1, j=2, then breaks
# The outer loop always completes all 3 rounds!


# ─────────────────────────────────────────────────────────
# SECTION 9: NESTED LOOP — CHECKLIST
# ─────────────────────────────────────────────────────────
# Before writing a nested loop, ask yourself:
#   1. What is my OUTER collection? (the "big" grouping)
#   2. What is my INNER collection? (the "small" items per group)
#   3. What should happen for EACH combination?
#   4. How many total iterations? outer_count × inner_count

print("\n--- Quick combinations count demo ---")
days   = ["Mon", "Tue", "Wed"]
shifts = ["Morning", "Evening"]

total_combos = 0
for day in days:
    for shift in shifts:
        total_combos += 1
        print(f"{day} {shift}")

print(f"\nTotal combinations: {total_combos}")   # 3 × 2 = 6
