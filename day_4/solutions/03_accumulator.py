# ---------------------------------------------------------
# SOLUTION 3: ACCUMULATOR PATTERN 🪣
# ---------------------------------------------------------
# Accumulator = a variable you grow inside a loop
# (total += x, count += 1, list.append(x), ...).


# TASK 1: Average calculator WITHOUT sum().
scores = [78, 92, 67, 85, 100, 71]
total = 0
for s in scores:
    total += s
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.2f}")


# TASK 2: Count vowels in a user word.
word = input("Enter a word: ")
vowel_count = 0
for letter in word.lower():     # lower() so "A" counts the same as "a"
    if letter in "aeiou":
        vowel_count += 1
print(f"The word '{word}' has {vowel_count} vowel(s).")


# TASK 3: Filter numbers into two lists.
numbers = [3, -5, 8, -2, 0, -11, 14, 7, -1]
positives = []
negatives = []
for n in numbers:
    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)
print("Positives:", positives)
print("Negatives:", negatives)


# ⭐ BONUS CHALLENGE: Collect names until "done".
names = []
while True:
    entry = input("Enter a name (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    names.append(entry)

print("All names:", names)
print(f"Total: {len(names)}")
print("Sorted:", sorted(names))
