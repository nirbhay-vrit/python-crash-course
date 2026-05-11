# ---------------------------------------------------------
# SOLUTION 6: NESTED LOOPS 🪆
# ---------------------------------------------------------
# A loop inside another loop. The INNER loop runs in full every
# time the OUTER loop steps forward by one.


# TASK 1: Full multiplication table 1–10.
# print(..., end="\t") keeps items on the same line, separated by a tab.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} × {j}={i * j}", end="\t")
    print()                     # newline at the end of each row


# TASK 2: Star patterns.

# Pattern A (right triangle)
print("\nPattern A:")
for row in range(1, 6):         # 1..5 stars on each line
    print("* " * row)

# Pattern B (inverted triangle)
print("\nPattern B:")
for row in range(5, 0, -1):     # 5..1
    print("* " * row)


# TASK 3: Seating Chart — 3 rows × 4 seats.
print("\nSeating Chart:")
for row in range(1, 4):
    for seat in range(1, 5):
        print(f"Row {row}, Seat {seat}")


# ⭐ BONUS CHALLENGE: Times-table quiz.
score = 0
for a in range(2, 6):           # 2..5
    for b in range(1, 6):       # 1..5
        try:
            answer = int(input(f"What is {a} × {b}? "))
        except ValueError:
            answer = None
        if answer == a * b:
            print("✅")
            score += 1
        else:
            print(f"❌ (answer was {a * b})")
print(f"\nFinal score: {score} / {4 * 5}")
