# ---------------------------------------------------------
# SOLUTION 1: FOR LOOP BASICS 🔄
# ---------------------------------------------------------


# TASK 1: Loop through a list of favourites.
# `for X in list:` runs the body once for every item in the list.
favourites = ["pizza", "chess", "anime", "guitar", "coffee"]
for thing in favourites:
    print(f"I really like: {thing}")


# TASK 2: Length reporter.
words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
for word in words:
    print(f"{word} → {len(word)} letters")


# TASK 3: Shopping bill — classic accumulator pattern.
prices = [120, 45, 80, 200, 60]
total = 0                       # start at 0
for price in prices:
    print(f"Item price: {price}")
    total += price              # grow the total
print(f"Total: {total}")


# ⭐ BONUS CHALLENGE: Celsius → Fahrenheit conversion table.
temps_c = [0, 20, 37, 100, -10]
for c in temps_c:
    f = (c * 9 / 5) + 32
    print(f"{c}°C = {f}°F")
