# ---------------------------------------------------------
# DAY 4 | TOPIC 2: range() — Loop a Specific Number of Times
# range() generates a sequence of numbers for your loop!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: range(n) — COUNT FROM 0 UP TO (BUT NOT INCLUDING) n
# ─────────────────────────────────────────────────────────
# This is the most common form. range(5) gives: 0, 1, 2, 3, 4
print("--- range(5) ---")
for i in range(5):
    print(i)

# Remember: starts at 0, stops BEFORE 5.
# Think of it like: [0, 1, 2, 3, 4]


# ─────────────────────────────────────────────────────────
# SECTION 2: range(start, stop) — CHOOSE WHERE TO START
# ─────────────────────────────────────────────────────────
# range(1, 6) gives: 1, 2, 3, 4, 5
# The start is INCLUDED. The stop is NOT included.
print("\n--- range(1, 6) ---")
for i in range(1, 6):
    print(i)

# Printing a multiplication table from 1 to 10:
print("\n--- 5 times table ---")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")


# ─────────────────────────────────────────────────────────
# SECTION 3: range(start, stop, step) — SKIP BY A STEP
# ─────────────────────────────────────────────────────────
# range(0, 11, 2) gives: 0, 2, 4, 6, 8, 10  (every 2nd number)
print("\n--- range(0, 11, 2) — even numbers ---")
for i in range(0, 11, 2):
    print(i, end="  ")   # end=" " keeps everything on one line
print()

# Odd numbers:
print("\n--- range(1, 11, 2) — odd numbers ---")
for i in range(1, 11, 2):
    print(i, end="  ")
print()

# Count by 10s:
print("\n--- range(0, 101, 10) — count by 10s ---")
for i in range(0, 101, 10):
    print(i, end="  ")
print()


# ─────────────────────────────────────────────────────────
# SECTION 4: COUNTING DOWN — use a NEGATIVE step
# ─────────────────────────────────────────────────────────
print("\n--- Countdown! ---")
for i in range(10, 0, -1):   # start=10, stop before 0, step=-1
    print(f"T minus {i}...")
print("Liftoff! 🚀")


# ─────────────────────────────────────────────────────────
# SECTION 5: USING range() TO INDEX A LIST
# ─────────────────────────────────────────────────────────
# Sometimes you need BOTH the index number AND the item.
students = ["Alice", "Bob", "Charlie", "Diana"]

print("\n--- With position numbers ---")
for i in range(len(students)):        # i goes 0, 1, 2, 3
    print(f"Seat {i + 1}: {students[i]}")

# Bonus: enumerate() does the same thing more cleanly
print("\n--- Same with enumerate() ---")
for i, student in enumerate(students, start=1):
    print(f"Seat {i}: {student}")
