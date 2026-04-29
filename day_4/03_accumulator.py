# ---------------------------------------------------------
# DAY 4 | TOPIC 3: THE ACCUMULATOR PATTERN 🪣
# The most important loop pattern: start with a "bucket",
# fill it up a little each round of the loop!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: SUMMING NUMBERS
# ─────────────────────────────────────────────────────────
# Pattern: create a variable BEFORE the loop, update it INSIDE.

prices = [120, 250, 75, 340, 99, 15, 200]

total = 0           # ← the "bucket" — starts empty (zero)

for price in prices:
    total += price  # ← add each price into the bucket
    # same as: total = total + price

print(f"Items: {prices}")
print(f"Total: Rs. {total}")


# ─────────────────────────────────────────────────────────
# SECTION 2: COUNTING ITEMS THAT MATCH A CONDITION
# ─────────────────────────────────────────────────────────
scores = [85, 42, 91, 38, 77, 55, 88, 29, 95, 60]

passing = 0         # bucket starts at 0

for score in scores:
    if score >= 60:
        passing += 1  # only count if the score passes

print(f"\nScores: {scores}")
print(f"Passing (60+): {passing} out of {len(scores)}")


# ─────────────────────────────────────────────────────────
# SECTION 3: FINDING THE MAXIMUM (without using max())
# ─────────────────────────────────────────────────────────
# Imagine going through a list and keeping track of the
# biggest number you've seen so far.

numbers = [34, 78, 12, 99, 56, 23, 88]
biggest = numbers[0]   # start by assuming first is biggest

for num in numbers:
    if num > biggest:
        biggest = num  # found a new champion!

print(f"\nNumbers: {numbers}")
print(f"Biggest: {biggest}")


# ─────────────────────────────────────────────────────────
# SECTION 4: BUILDING A STRING CHARACTER BY CHARACTER
# ─────────────────────────────────────────────────────────
# Strings can be "accumulated" too — start with "", add each piece.

word = "python"
reversed_word = ""    # empty string bucket

for letter in word:
    reversed_word = letter + reversed_word  # add letter to the FRONT

print(f"\nOriginal : {word}")
print(f"Reversed : {reversed_word}")


# ─────────────────────────────────────────────────────────
# SECTION 5: BUILDING A NEW LIST (filtering)
# ─────────────────────────────────────────────────────────
# Keep only the items you want by appending into a new list.

all_marks = [45, 82, 30, 91, 55, 74, 28, 66]
high_scorers = []     # empty list bucket

for mark in all_marks:
    if mark >= 70:
        high_scorers.append(mark)

print(f"\nAll marks   : {all_marks}")
print(f"High scorers: {high_scorers}")


# ─────────────────────────────────────────────────────────
# SECTION 6: PUTTING IT ALL TOGETHER — CLASS REPORT
# ─────────────────────────────────────────────────────────
student_scores = {
    "Alice": 88, "Bob": 45, "Charlie": 92,
    "Diana": 57, "Eve": 76, "Frank": 33
}

total_score = 0
pass_count  = 0

print("\n--- Class Report ---")
for student, score in student_scores.items():
    status = "PASS ✅" if score >= 60 else "FAIL ❌"
    print(f"  {student:<10} {score:>3}  {status}")
    total_score += score
    if score >= 60:
        pass_count += 1

average = total_score / len(student_scores)
print(f"\nClass average : {average:.1f}")
print(f"Students passed: {pass_count} / {len(student_scores)}")
