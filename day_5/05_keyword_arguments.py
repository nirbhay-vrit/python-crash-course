# ---------------------------------------------------------
# DAY 5 | TOPIC 5: KEYWORD ARGUMENTS — Name Your Values 🏷️
# Pass arguments by name to make code clearer and more flexible!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: POSITIONAL VS KEYWORD ARGUMENTS
# ─────────────────────────────────────────────────────────
# Positional: order matters! First arg → first parameter.
# Keyword: name matters! You specify which parameter gets which value.

def describe_pet(pet_name, animal_type, age):
    print(f"{pet_name} is a {age}-year-old {animal_type}.")

print("--- Positional (order matters) ---")
describe_pet("Fluffy", "cat", 3)

print("\n--- Keyword (names matter, order doesn't) ---")
describe_pet(animal_type="dog", age=5, pet_name="Rex")
describe_pet(age=2, pet_name="Goldie", animal_type="fish")


# ─────────────────────────────────────────────────────────
# SECTION 2: MIXING POSITIONAL AND KEYWORD
# ─────────────────────────────────────────────────────────
# Positional arguments MUST come before keyword arguments.

def make_pizza(size, crust, topping1, topping2):
    print(f"{size} {crust} crust pizza with {topping1} and {topping2}")

print("\n--- Mixing positional and keyword ---")
make_pizza("large", "thin", "pepperoni", "mushrooms")  # all positional
make_pizza("medium", "thick", topping2="olives", topping1="onions")  # mix

# This would be WRONG: make_pizza(size="small", "thin", ...)
# Positional cannot come after keyword!


# ─────────────────────────────────────────────────────────
# SECTION 3: KEYWORD ARGUMENTS MAKE CODE CLEARER
# ─────────────────────────────────────────────────────────
# With many parameters, keywords tell you what each value means.

def create_user(username, email, is_active, is_admin, created_date):
    status = "active" if is_active else "inactive"
    role = "admin" if is_admin else "user"
    print(f"{username} ({email}) - {status} {role}, joined {created_date}")

print("\n--- Clearer with keywords ---")
# Without keywords - what do these booleans mean?
# create_user("alice", "alice@email.com", True, False, "2024-01-15")  # unclear!

# With keywords - crystal clear!
create_user(
    username="alice",
    email="alice@email.com",
    is_active=True,
    is_admin=False,
    created_date="2024-01-15"
)


# ─────────────────────────────────────────────────────────
# SECTION 4: KEYWORD ARGUMENTS WITH DEFAULTS
# ─────────────────────────────────────────────────────────
# Combine keywords with defaults for maximum flexibility!

def book_flight(destination, origin="NYC", class_type="economy", meals=False):
    meal_text = "with meals" if meals else "no meals"
    print(f"Flight: {origin} → {destination} ({class_type}, {meal_text})")

print("\n--- Skipping optional parameters with keywords ---")
book_flight("Paris")                                    # all defaults
book_flight("Tokyo", class_type="business")            # skip origin, set class
book_flight("London", meals=True)                        # skip origin and class
book_flight("Sydney", origin="LAX", class_type="first", meals=True)


# ─────────────────────────────────────────────────────────
# SECTION 5: ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# ─────────────────────────────────────────────────────────
# Use **kwargs to accept ANY number of keyword arguments.
# Inside the function, kwargs is a dictionary!

def build_profile(first, last, **user_info):
    """Build a user profile with any additional information."""
    profile = {
        "first_name": first,
        "last_name": last,
    }
    # Add all the extra keyword arguments
    for key, value in user_info.items():
        profile[key] = value
    return profile

print("\n--- Using **kwargs ---")
user1 = build_profile("Ada", "Lovelace", field="math", century=19)
user2 = build_profile("Grace", "Hopper", field="CS", language="COBOL", rank="Rear Admiral")

print(user1)
print(user2)


# ─────────────────────────────────────────────────────────
# SECTION 6: WHEN TO USE WHAT?
# ─────────────────────────────────────────────────────────

def example(a, b, c=10, d=20):
    print(f"a={a}, b={b}, c={c}, d={d}")

print("\n--- Best practices ---")
# Required args (a, b) - positional is fine
example(1, 2)

# Optional args (c, d) - use keywords to be clear
example(1, 2, c=30)
example(1, 2, d=40)
example(1, 2, c=30, d=40)

# Rule of thumb:
# - 1-2 arguments: positional is fine
# - 3+ arguments or booleans: consider keywords for clarity
