# ---------------------------------------------------------
# DAY 4 | TOPIC 1: THE FOR LOOP — From Scratch 🔄
# A loop makes Python repeat code for you automatically!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM LOOPS SOLVE
# ─────────────────────────────────────────────────────────
# Imagine you want to greet 5 friends. WITHOUT a loop:
print("Hello, Alice!")
print("Hello, Bob!")
print("Hello, Charlie!")
print("Hello, Diana!")
print("Hello, Eve!")

# That's 5 lines. What if you had 100 friends?
# Loops let you write it ONCE and repeat it automatically.


# ─────────────────────────────────────────────────────────
# SECTION 2: YOUR FIRST FOR LOOP
# ─────────────────────────────────────────────────────────
# Read this out loud: "FOR each name IN this list, do this:"

friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

print("\n--- For loop greeting ---")
for name in friends:
    print(f"Hello, {name}!")

# That's just 2 lines — and it works for any number of friends!


# ─────────────────────────────────────────────────────────
# SECTION 3: UNDERSTANDING THE LOOP VARIABLE
# ─────────────────────────────────────────────────────────
# 'name' is called the LOOP VARIABLE.
# Python creates it automatically and fills it with the next
# item from the list every time the loop runs.
#
# Round 1: name = "Alice"   → prints "Hello, Alice!"
# Round 2: name = "Bob"     → prints "Hello, Bob!"
# Round 3: name = "Charlie" → prints "Hello, Charlie!"
# ... and so on until the list is finished.

# You can call the loop variable ANYTHING:
print("\n--- Same loop, different variable name ---")
for person in friends:           # 'person' instead of 'name'
    print(f"{person} is here.")

# Both loops do the same thing — the variable name is just a label.


# ─────────────────────────────────────────────────────────
# SECTION 4: THE INDENTED BLOCK — What goes "inside" the loop
# ─────────────────────────────────────────────────────────
# Everything indented under 'for' repeats every round.
# Everything NOT indented only runs ONCE (after the loop ends).

scores = [85, 92, 70, 55, 98]

print("\n--- Indentation matters! ---")
for score in scores:
    print(f"Score: {score}")          # ← INSIDE loop (repeats)
    print(f"  Grade check done.\n")   # ← INSIDE loop (repeats)

print("All scores reviewed.")         # ← OUTSIDE loop (runs once)


# ─────────────────────────────────────────────────────────
# SECTION 5: MULTIPLE STATEMENTS INSIDE THE LOOP
# ─────────────────────────────────────────────────────────
# You can have as many lines as you want inside the loop body!

fruits = ["apple", "banana", "mango"]

print("--- Multiple lines in loop body ---")
for fruit in fruits:
    upper = fruit.upper()              # make it uppercase
    length = len(fruit)                # count the letters
    print(f"{upper} has {length} letters")
