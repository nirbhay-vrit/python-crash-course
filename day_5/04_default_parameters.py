# ---------------------------------------------------------
# DAY 5 | TOPIC 4: DEFAULT PARAMETERS — Making Arguments Optional 🎯
# Give parameters default values so callers can skip them!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM — TOO MANY ARGUMENTS
# ─────────────────────────────────────────────────────────
# What if you have a function that usually needs one value,
# but sometimes needs another?

def make_drink(drink_type, size):
    print(f"One {size} {drink_type} coming up!")

make_drink("coffee", "medium")
make_drink("tea", "large")

# Every caller MUST provide both. What if most people want "medium"?


# ─────────────────────────────────────────────────────────
# SECTION 2: DEFAULT VALUES
# ─────────────────────────────────────────────────────────
# Assign a default value in the function definition.
# If the caller doesn't provide that argument, the default is used.

def greet(name="friend"):       # "friend" is the default
    print(f"Hello, {name}!")

print("\n--- Using default parameter ---")
greet("Alice")      # Uses the argument: "Hello, Alice!"
greet()             # Uses default: "Hello, friend!"
greet("Bob")        # Uses the argument: "Hello, Bob!"


# ─────────────────────────────────────────────────────────
# SECTION 3: MULTIPLE PARAMETERS WITH DEFAULTS
# ─────────────────────────────────────────────────────────
# You can mix required and optional parameters.
# REQUIRED parameters must come BEFORE optional ones!

def make_smoothie(fruit, size="medium", ice=True):
    ice_text = "with ice" if ice else "no ice"
    print(f"{size} {fruit} smoothie ({ice_text})")

print("\n--- Mixing required and optional ---")
make_smoothie("mango")                    # mango, medium, with ice
make_smoothie("banana", "large")          # banana, large, with ice
make_smoothie("strawberry", "small", False)  # strawberry, small, no ice


# ─────────────────────────────────────────────────────────
# SECTION 4: DEFAULTS MAKE FUNCTIONS FLEXIBLE
# ─────────────────────────────────────────────────────────
# Good defaults reduce typing for common cases.

def send_message(text, urgency="normal", signature=""):
    print(f"[{urgancy.upper()}] {text}")
    if signature:
        print(f"  — {signature}")

print("\n--- Flexible messaging ---")
send_message("Meeting at 3pm")
send_message("Server down!", "high")
send_message("Project complete", "normal", "The Dev Team")


# ─────────────────────────────────────────────────────────
# SECTION 5: COMMON DEFAULT PATTERNS
# ─────────────────────────────────────────────────────────
# Empty string, zero, None, and empty list are common defaults.

def calculate_total(items, tax_rate=0.0, discount=0):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax - discount
    return total

print("\n--- Default calculations ---")
print(calculate_total([10, 20, 30]))              # No tax, no discount
print(calculate_total([10, 20, 30], 0.08))        # 8% tax
print(calculate_total([10, 20, 30], 0.08, 5))     # 8% tax, $5 off


# ─────────────────────────────────────────────────────────
# SECTION 6: GOTCHA — Mutable Default Arguments
# ─────────────────────────────────────────────────────────
# NEVER use mutable defaults like [] or {}!
# They are created ONCE and shared between all calls.

# WRONG WAY (don't do this):
def add_item_wrong(new_item, item_list=[]):    # DANGER! Shared list!
    item_list.append(new_item)
    return item_list

# RIGHT WAY:
def add_item_right(new_item, item_list=None):  # Use None as default
    if item_list is None:
        item_list = []                           # Create new list each call
    item_list.append(new_item)
    return item_list

print("\n--- Correct mutable default pattern ---")
result1 = add_item_right("apple")
print(result1)        # ["apple"]
result2 = add_item_right("banana")
print(result2)        # ["banana"] (correct! new list each time)
