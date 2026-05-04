# ---------------------------------------------------------
# DAY 6 | TOPIC 1: MULTIPLE RETURN VALUES 🎁
# A function can return more than one value at once!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: QUICK REVIEW — RETURNING ONE VALUE
# ─────────────────────────────────────────────────────────
# So far, return sends back a single piece of data.

def get_greeting(name):
    return f"Hello, {name}!"

message = get_greeting("Alice")
print(message)   # Hello, Alice!


# ─────────────────────────────────────────────────────────
# SECTION 2: RETURNING TWO VALUES
# ─────────────────────────────────────────────────────────
# Python lets you return multiple values separated by commas.
# Under the hood, Python packs them into a TUPLE.

def min_and_max(numbers):
    smallest = min(numbers)
    largest  = max(numbers)
    return smallest, largest    # ← two values, one return

scores = [45, 88, 23, 97, 61]
result = min_and_max(scores)

print("\n--- Returning two values ---")
print(result)         # (23, 97)  ← it's a tuple!
print(type(result))   # <class 'tuple'>


# ─────────────────────────────────────────────────────────
# SECTION 3: UNPACKING MULTIPLE RETURN VALUES
# ─────────────────────────────────────────────────────────
# You can unpack the tuple into separate variables on one line.
# This is clean and readable — you'll see this pattern everywhere.

low, high = min_and_max(scores)

print("\n--- Unpacking return values ---")
print(f"Lowest: {low}")    # Lowest: 23
print(f"Highest: {high}")  # Highest: 97


def get_name_and_age():
    return "Bob", 30

name, age = get_name_and_age()
print(f"\n{name} is {age} years old.")    # Bob is 30 years old.


# ─────────────────────────────────────────────────────────
# SECTION 4: RETURNING THREE OR MORE VALUES
# ─────────────────────────────────────────────────────────
# There's no limit to how many values you can return.

def circle_stats(radius):
    import math
    area      = math.pi * radius ** 2
    diameter  = 2 * radius
    circumference = 2 * math.pi * radius
    return area, diameter, circumference

area, diam, circ = circle_stats(5)

print("\n--- Circle with radius 5 ---")
print(f"Area:          {area:.2f}")
print(f"Diameter:      {diam}")
print(f"Circumference: {circ:.2f}")


# ─────────────────────────────────────────────────────────
# SECTION 5: PRACTICAL EXAMPLE — SPLIT A SENTENCE
# ─────────────────────────────────────────────────────────
# A function that analyses a sentence and returns multiple stats.

def analyse_sentence(sentence):
    words      = sentence.split()
    word_count = len(words)
    char_count = len(sentence)
    longest    = max(words, key=len)
    return word_count, char_count, longest

sentence = "The quick brown fox jumps over the lazy dog"
words, chars, longest_word = analyse_sentence(sentence)

print("\n--- Sentence analysis ---")
print(f"Words:        {words}")
print(f"Characters:   {chars}")
print(f"Longest word: {longest_word}")


# ─────────────────────────────────────────────────────────
# SECTION 6: THE VARIABLE SWAP TRICK
# ─────────────────────────────────────────────────────────
# Python's tuple unpacking allows a famous one-liner swap!

a = 10
b = 20

print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a    # ← swap using multiple assignment (same idea!)
print(f"After swap:  a = {a}, b = {b}")
