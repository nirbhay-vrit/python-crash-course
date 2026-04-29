# ---------------------------------------------------------
# DAY 4 | TOPIC 6: NESTED LOOPS — A Loop Inside a Loop 🪆
# For every round of the OUTER loop, the INNER loop runs completely!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE CONCEPT — OUTER × INNER
# ─────────────────────────────────────────────────────────
# Think of a clock: the minute hand (inner) goes all the way
# around every time the hour hand (outer) moves one step.

print("--- 3 × 3 example ---")
for i in range(1, 4):            # outer: 1, 2, 3
    for j in range(1, 4):        # inner: 1, 2, 3 (runs FULLY each outer round)
        print(f"  ({i}, {j})")
    print()                      # blank line after each outer round

# Total: 3 × 3 = 9 pairs printed


# ─────────────────────────────────────────────────────────
# SECTION 2: MULTIPLICATION TABLE
# ─────────────────────────────────────────────────────────
print("--- Multiplication Table (1–5) ---")
print("    ", end="")
for col in range(1, 6):
    print(f"{col:>4}", end="")   # print header row
print("\n    " + "─" * 20)

for row in range(1, 6):
    print(f"{row:>3} |", end="")
    for col in range(1, 6):
        print(f"{row * col:>4}", end="")   # :>4 = right-align in 4 spaces
    print()                                # new line after each row


# ─────────────────────────────────────────────────────────
# SECTION 3: STAR PATTERNS
# ─────────────────────────────────────────────────────────
# A classic nested loop exercise — great for understanding the pattern.

rows = 5

print("\n--- Square ---")
for i in range(rows):
    for j in range(rows):
        print("★ ", end="")
    print()

print("\n--- Right triangle ---")
for i in range(1, rows + 1):
    for j in range(i):     # inner loop runs i times (grows each row)
        print("★ ", end="")
    print()

print("\n--- Pyramid ---")
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")    # leading spaces
    for j in range(2 * i - 1):        # stars per row: 1, 3, 5, 7, 9
        print("★", end="")
    print()


# ─────────────────────────────────────────────────────────
# SECTION 4: REAL USE — COMPARE EVERY PAIR IN A LIST
# ─────────────────────────────────────────────────────────
# Find all pairs of students with the same score.
students = [("Alice", 85), ("Bob", 72), ("Charlie", 85), ("Diana", 91), ("Eve", 72)]

print("\n--- Students with matching scores ---")
for i in range(len(students)):
    for j in range(i + 1, len(students)):    # j starts AFTER i (avoid repeats)
        name1, score1 = students[i]
        name2, score2 = students[j]
        if score1 == score2:
            print(f"  {name1} and {name2} both scored {score1}")
