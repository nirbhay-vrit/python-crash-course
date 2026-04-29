# ---------------------------------------------------------
# DAY 4 | TOPIC 4: THE WHILE LOOP — Keep Going Until... 🔁
# A while loop repeats AS LONG AS a condition stays True!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: HOW A WHILE LOOP WORKS
# ─────────────────────────────────────────────────────────
#
#   Step 1: Check the condition
#   Step 2: If True  → run the block, then go back to Step 1
#   Step 3: If False → skip the block, continue after the loop
#
# Key difference from for:
#   for  → you know how many items / repetitions upfront
#   while → you keep going until something CHANGES

print("--- Countdown with while ---")
countdown = 5

while countdown > 0:          # check: is countdown > 0?
    print(f"T minus {countdown}...")
    countdown -= 1             # CRITICAL: change the variable!

print("Liftoff! 🚀")

# Trace through:
# countdown=5 → 5>0 True  → print, countdown becomes 4
# countdown=4 → 4>0 True  → print, countdown becomes 3
# countdown=3 → 3>0 True  → print, countdown becomes 2
# countdown=2 → 2>0 True  → print, countdown becomes 1
# countdown=1 → 1>0 True  → print, countdown becomes 0
# countdown=0 → 0>0 FALSE → exit loop, print "Liftoff!"


# ─────────────────────────────────────────────────────────
# SECTION 2: WHILE LOOP WITH USER INPUT
# ─────────────────────────────────────────────────────────
# Perfect when you don't know how many tries the user needs.

print("\n--- Password with retry ---")
secret = "python"
attempts = 0

guess = input("Enter password: ")
attempts += 1

while guess != secret:
    print("Wrong! Try again.")
    guess = input("Enter password: ")
    attempts += 1

print(f"Correct! You got it in {attempts} attempt(s). 🎉")


# ─────────────────────────────────────────────────────────
# SECTION 3: CONTROLLING ATTEMPTS WITH A COUNTER
# ─────────────────────────────────────────────────────────
# Combine a while loop with a counter to limit attempts.

print("\n--- Limited attempts ---")
secret_pin = "1234"
max_attempts = 3
tries = 0

while tries < max_attempts:
    pin = input(f"Enter PIN (attempt {tries + 1}/{max_attempts}): ")
    tries += 1
    if pin == secret_pin:
        print("Access granted! 🔓")
        break                    # exit the loop immediately
else:
    # The 'else' after while runs ONLY if the loop finished
    # without hitting a 'break' (i.e., all attempts used up)
    print("Account locked after 3 failed attempts! 🔒")


# ─────────────────────────────────────────────────────────
# SECTION 4: FLAG VARIABLE — A CLEAN while PATTERN
# ─────────────────────────────────────────────────────────
# A flag is a boolean that controls the loop.

print("\n--- Mini calculator (type 'quit' to exit) ---")
running = True                  # flag starts True

while running:
    entry = input("Enter a number (or 'quit'): ")

    if entry == "quit":
        running = False         # set flag to False → loop stops
    else:
        try:
            number = float(entry)
            print(f"  → {number} squared = {number ** 2}")
        except ValueError:
            print("  That's not a number!")

print("Calculator closed. Goodbye!")
