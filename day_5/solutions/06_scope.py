# ---------------------------------------------------------
# SOLUTION 6: SCOPE 🌍
# ---------------------------------------------------------
# Scope = the region of code where a variable is visible.
# Local variables (defined inside a function) ONLY exist inside it.
# Global variables (defined at module level) are visible everywhere.


# TASK 1: Local vs Global.
secret = "global secret"

def mystery():
    secret = "local secret"     # NEW local variable that shadows the global
    print(secret)

print(secret)       # → "global secret"   (the local doesn't exist yet)
mystery()           # → "local secret"    (uses the local)
print(secret)       # → "global secret"   (the local is gone now)


# TASK 2: Why it broke + fix with `global`.
count = 0

def increment():
    global count                # tell Python: "I want to modify the GLOBAL `count`"
    count += 1
    print(count)

increment()         # 1
increment()         # 2


# TASK 3: Better counter — no `global`, just parameter + return.
# This is the preferred way: functions take input, give output, no hidden state.
def increment_value(current):
    return current + 1

count2 = 0
count2 = increment_value(count2)   # 1
count2 = increment_value(count2)   # 2
print(count2)


# TASK 4: Calculator with constants.
# UPPER_CASE names by convention mean "constant — don't change".
TAX_RATE = 0.08
SHIPPING_COST = 5.0

def calculate_total(subtotal):
    return subtotal + (subtotal * TAX_RATE) + SHIPPING_COST

print(calculate_total(50))      # 50 + 4 + 5 = 59.0
print(calculate_total(100))     # 100 + 8 + 5 = 113.0


# TASK 5: Shadowing.
score = 100

def play_game():
    score = 50                  # local — shadows the global "score"
    print(f"Local score: {score}")
    return score

result = play_game()
print(f"Returned: {result}")
print(f"Global score: {score}")   # global is still 100, untouched


# ⭐ BONUS CHALLENGE: Counter using nested functions + nonlocal.
# The outer function holds the state; the inner function modifies it.
def create_counter():
    count = 0                   # this lives in the OUTER function

    def increment():
        nonlocal count          # refer to `count` in the enclosing scope
        count += 1
        return count

    return increment            # return the inner function

counter = create_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
# Each call updates the SAME `count` — no globals, no class needed.
