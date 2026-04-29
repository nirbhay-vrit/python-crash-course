# ---------------------------------------------------------
# DAY 4 | TOPIC 5: break & continue — Controlling Loops 🎮
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: break — EXIT THE LOOP IMMEDIATELY
# ─────────────────────────────────────────────────────────
# break jumps OUT of the loop right now, no questions asked.
# The rest of the loop body AND any remaining rounds are skipped.

print("--- break: stop when we find 'mango' ---")
fruits = ["apple", "banana", "mango", "orange", "kiwi"]

for fruit in fruits:
    if fruit == "mango":
        print(f"Found mango! Stopping search.")
        break                 # exit the loop
    print(f"Checked: {fruit}")

# Output:
# Checked: apple
# Checked: banana
# Found mango! Stopping search.
# (orange and kiwi are NEVER checked)


# ─────────────────────────────────────────────────────────
# SECTION 2: continue — SKIP THIS ROUND, GO TO THE NEXT
# ─────────────────────────────────────────────────────────
# continue skips the REST of the current round and jumps
# straight to the NEXT iteration. The loop does NOT stop.

print("\n--- continue: skip negative numbers ---")
numbers = [4, -2, 7, -5, 10, -1, 8]

for num in numbers:
    if num < 0:
        continue           # skip negative, go to next number
    print(f"Positive: {num}")

# Output: 4, 7, 10, 8  (negatives are skipped but loop continues)


# ─────────────────────────────────────────────────────────
# SECTION 3: break vs continue — SIDE BY SIDE
# ─────────────────────────────────────────────────────────
# break  → "I'm done. EXIT the whole loop."
# continue → "Skip this one item. Keep going with the next."

data = [1, 2, -99, 4, 5]

print("\n--- break at -99 ---")
for x in data:
    if x == -99:
        break
    print(x)          # prints: 1, 2

print("\n--- continue at -99 ---")
for x in data:
    if x == -99:
        continue
    print(x)          # prints: 1, 2, 4, 5


# ─────────────────────────────────────────────────────────
# SECTION 4: break IN A WHILE LOOP
# ─────────────────────────────────────────────────────────
# break is especially useful with while True: (an intentional
# "run forever" loop that you exit with break).

print("\n--- while True with break ---")
while True:                    # runs forever... until break!
    answer = input("Type 'yes' to continue or 'no' to stop: ").lower()
    if answer == "no":
        print("Goodbye!")
        break
    elif answer == "yes":
        print("Great, continuing!")
    else:
        print("Please type 'yes' or 'no'.")


# ─────────────────────────────────────────────────────────
# SECTION 5: PRACTICAL — SEARCH IN A LIST
# ─────────────────────────────────────────────────────────
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = input("\nWhich student are you looking for? ")

found = False

for student in students:
    if student.lower() == target.lower():
        print(f"Found {student} in the list! ✅")
        found = True
        break

if not found:
    print(f"{target} is not in the list. ❌")
