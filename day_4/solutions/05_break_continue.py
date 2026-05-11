# ---------------------------------------------------------
# SOLUTION 5: break & continue 🎮
# ---------------------------------------------------------
# break    → exit the loop completely
# continue → skip the REST of this iteration, go to the next one


# TASK 1: First negative number in the list.
numbers = [10, 25, 8, -3, 14, -7, 20]
found = False
for n in numbers:
    if n < 0:
        print(f"First negative number: {n}")
        found = True
        break                   # stop as soon as we find one
if not found:
    print("No negative numbers.")


# TASK 2: Skip banned words with continue.
words = ["hello", "spam", "world", "click", "python", "buy", "now"]
banned = ["spam", "click", "buy"]
for word in words:
    if word in banned:
        continue                # skip — don't print, jump to next word
    print(word)


# TASK 3: Input Validator — keep asking until input is valid.
while True:
    raw = input("Enter a number between 1 and 10: ")
    # Method 1: check that all characters are digits before int().
    if not raw.isdigit():
        print("That's not a number!")
        continue
    value = int(raw)
    if 1 <= value <= 10:
        print(f"Great! You entered: {value}")
        break
    else:
        print("Out of range — try again.")


# ⭐ BONUS CHALLENGE: predicting outputs.

# Loop A:
#   1 (odd, printed) — 2 skipped (continue) — 3 printed — 4 skipped
#   5 printed — 6 skipped — 7 > 5 so break.
# Expected: 1, 3, 5
for i in range(1, 8):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print(i)

# Loop B:
#   total starts at 0. Add 10 (10), add 20 (30), add 30 (60).
#   Next check: 60 >= 50 → break. We never add 40 or 50.
# Expected: 60
total = 0
for n in [10, 20, 30, 40, 50]:
    if total >= 50:
        break
    total += n
print(total)
