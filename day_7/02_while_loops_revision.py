# ---------------------------------------------------------
# DAY 7 | REVISION 2: WHILE LOOPS — Keep Going Until... 🔁
# A while loop keeps running AS LONG AS something is True.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: FOR vs WHILE — Which one to use?
# ─────────────────────────────────────────────────────────
#
#  FOR loop  → you KNOW how many times to repeat upfront.
#              e.g., "go through every name in this list"
#
#  WHILE loop → you KEEP GOING until a condition changes.
#              e.g., "keep asking until the user says 'quit'"
#
# Think of while like a security guard at a door:
#   "While the door is locked, keep checking the key."
#   The moment the key is correct → the condition becomes False → stop.


# ─────────────────────────────────────────────────────────
# SECTION 2: YOUR FIRST WHILE LOOP
# ─────────────────────────────────────────────────────────
# Syntax:
#   while <condition is True>:
#       <do something>
#       <change something so eventually it becomes False!>

print("--- Countdown ---")
count = 5

while count > 0:       # keep going AS LONG AS count > 0
    print(count)
    count -= 1         # IMPORTANT: reduce count by 1 each time!

print("Go!")

# Trace through step by step:
# count=5 → 5>0? YES → print 5 → count becomes 4
# count=4 → 4>0? YES → print 4 → count becomes 3
# count=3 → 3>0? YES → print 3 → count becomes 2
# count=2 → 2>0? YES → print 2 → count becomes 1
# count=1 → 1>0? YES → print 1 → count becomes 0
# count=0 → 0>0? NO  → EXIT loop → print "Go!"


# ─────────────────────────────────────────────────────────
# SECTION 3: THE INFINITE LOOP — THE BIGGEST MISTAKE
# ─────────────────────────────────────────────────────────
# If you forget to change the variable, the loop runs FOREVER.
# This is called an INFINITE LOOP. Press Ctrl+C to stop it.
#
#   BAD (runs forever — DO NOT run this!):
#   count = 5
#   while count > 0:
#       print(count)
#       # ← forgot count -= 1 !!! loop never stops
#
# RULE: Always make sure the condition can eventually become False.

print("\n--- Good pattern: always change something ---")
number = 1

while number <= 5:
    print(f"number is {number}")
    number += 1        # ← this ensures the loop will end

print("Loop finished!")


# ─────────────────────────────────────────────────────────
# SECTION 4: WHILE LOOP WITH USER INPUT
# ─────────────────────────────────────────────────────────
# Perfect when you don't know how many tries the user needs.

print("\n--- Guess the number ---")
secret = 7
guess = 0             # start with a wrong guess to enter the loop

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")

print("You got it!")


# ─────────────────────────────────────────────────────────
# SECTION 5: USING break — Exit the loop early
# ─────────────────────────────────────────────────────────
# break immediately exits the loop, no matter what the condition is.

print("\n--- Search and stop when found ---")
items = ["pen", "book", "eraser", "ruler", "scissors"]
looking_for = "eraser"

for item in items:
    if item == looking_for:
        print(f"Found it: {item}")
        break                       # stop searching — we found it!
    print(f"Not this one: {item}")


# ─────────────────────────────────────────────────────────
# SECTION 6: USING continue — Skip one round
# ─────────────────────────────────────────────────────────
# continue jumps to the NEXT round of the loop, skipping the rest.

print("\n--- Print only even numbers ---")
for i in range(1, 11):
    if i % 2 != 0:       # if odd...
        continue         # ...skip this round
    print(i)             # only even numbers reach this line

# Output: 2  4  6  8  10


# ─────────────────────────────────────────────────────────
# SECTION 7: WHILE LOOP WITH A FLAG
# ─────────────────────────────────────────────────────────
# A 'flag' is a boolean variable that controls the loop.
# When you're ready to stop, set the flag to False.

print("\n--- Simple menu (flag pattern) ---")
running = True

while running:
    choice = input("\nMenu — (1) Say Hello  (2) Count to 5  (q) Quit: ")

    if choice == "1":
        print("Hello there!")
    elif choice == "2":
        for n in range(1, 6):
            print(n)
    elif choice == "q":
        running = False     # ← set flag to False → loop ends
    else:
        print("Unknown option.")

print("Goodbye!")


# ─────────────────────────────────────────────────────────
# SECTION 8: WHILE LOOP — Collecting input until done
# ─────────────────────────────────────────────────────────
# A common real-world pattern: keep collecting items until the
# user types something special (like 'done').

print("\n--- Build a shopping list ---")
shopping_list = []

print("Enter items. Type 'done' when finished.")
while True:                         # runs forever UNTIL break
    item = input("Add item: ")
    if item == "done":
        break                       # user is done — exit loop
    shopping_list.append(item)
    print(f"  Added: {item}")

print(f"\nYour list: {shopping_list}")
