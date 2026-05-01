# ---------------------------------------------------------
# DAY 5 | TOPIC 6: SCOPE — Where Variables Live 🌍
# Variables can be LOCAL (inside a function) or GLOBAL (everywhere).
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: LOCAL VARIABLES
# ─────────────────────────────────────────────────────────
# Variables created INSIDE a function only exist there.
# They are "born" when the function starts and "die" when it ends.

def make_sandwich():
    bread = "sourdough"      # LOCAL variable - only exists in this function!
    filling = "cheese"
    print(f"Making a {filling} sandwich on {bread}")

make_sandwich()
# print(bread)    # ERROR! 'bread' is not defined outside the function

print("\n--- Local variables are temporary ---")

def count_to_three():
    number = 1               # 'number' is local
    while number <= 3:
        print(number)
        number += 1
    # 'number' disappears here!

count_to_three()
count_to_three()            # Each call gets a fresh 'number'


# ─────────────────────────────────────────────────────────
# SECTION 2: GLOBAL VARIABLES
# ─────────────────────────────────────────────────────────
# Variables created OUTSIDE all functions exist everywhere.
# Both the main code and functions can read them.

player_name = "Hero"         # GLOBAL variable
score = 0                    # GLOBAL variable

def show_status():
    print(f"{player_name}'s score: {score}")  # Reading global - OK!

print("\n--- Global variables are shared ---")
show_status()
score = 100
show_status()


# ─────────────────────────────────────────────────────────
# SECTION 3: THE SHADOWING PROBLEM
# ─────────────────────────────────────────────────────────
# If a local variable has the same name as a global,
# the LOCAL one "shadows" (hides) the global one inside the function.

message = "I am global"      # Global

def demo_shadowing():
    message = "I am local"   # LOCAL 'message' shadows global
    print(message)           # Prints the LOCAL one

def demo_no_shadowing():
    print(message)           # No local 'message', so uses GLOBAL

print("\n--- Shadowing ---")
print(message)               # "I am global"
demo_shadowing()             # "I am local"
print(message)               # Still "I am global" (unchanged!)
demo_no_shadowing()          # "I am global"


# ─────────────────────────────────────────────────────────
# SECTION 4: MODIFYING GLOBALS (THE 'global' KEYWORD)
# ─────────────────────────────────────────────────────────
# To CHANGE a global variable inside a function, use 'global'.
# This tells Python: "I mean the global one, not a local!"

total_points = 0

def add_points(points):
    global total_points      # We're going to use the GLOBAL total_points
    total_points += points   # Now this modifies the global variable!
    print(f"Added {points}. Total: {total_points}")

print("\n--- Using 'global' to modify ---")
add_points(10)
add_points(25)
print(f"Final total: {total_points}")  # 35


# ─────────────────────────────────────────────────────────
# SECTION 5: BEST PRACTICE — AVOID 'global'
# ─────────────────────────────────────────────────────────
# Using 'global' makes code hard to follow. Better: use return!

counter_good = 0

def increment_good(current):   # Take value as parameter
    return current + 1         # Return new value

counter_good = increment_good(counter_good)  # 1
counter_good = increment_good(counter_good)  # 2

print(f"\n--- Better: use return, not global ---")
print(f"Counter: {counter_good}")


# ─────────────────────────────────────────────────────────
# SECTION 6: CONSTANTS (UPPERCASE GLOBALS)
# ─────────────────────────────────────────────────────────
# Use ALL_CAPS for values that never change.
# These are called "constants".

PI = 3.14159
MAX_PLAYERS = 4
GAME_TITLE = "Python Adventure"

def circle_area(radius):
    return PI * radius * radius   # Reading constant - OK!

def can_join_game(current_players):
    return current_players < MAX_PLAYERS

print(f"\n--- Constants ---")
print(f"Area of radius 5: {circle_area(5):.2f}")
print(f"Can join with 3 players? {can_join_game(3)}")
