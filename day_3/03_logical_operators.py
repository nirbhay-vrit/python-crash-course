# ---------------------------------------------------------
# DAY 3 | TOPIC 3: LOGICAL OPERATORS — and, or, not 🔗
# Combine multiple conditions into one!
# ---------------------------------------------------------


# 1. THE THREE LOGICAL OPERATORS
#
#   and  →  BOTH conditions must be True
#   or   →  AT LEAST ONE condition must be True
#   not  →  FLIPS True to False (and vice versa)


# 2. AND — both must be True
print("--- and ---")
age = 20
has_id = True

if age >= 18 and has_id:
    print("Welcome! You may enter.")
else:
    print("Entry denied.")

# Try: age = 15, has_id = True  → denied (age fails)
# Try: age = 20, has_id = False → denied (id fails)
# Try: age = 20, has_id = True  → welcome!


# 3. OR — at least one must be True
print("\n--- or ---")
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("You get a 20% discount!")
else:
    print("No discount available.")


# 4. NOT — flips the boolean
print("\n--- not ---")
is_raining = False

if not is_raining:
    print("Great day for a walk! ☀️")
else:
    print("Stay inside — it's raining! 🌧️")

# 'not False' becomes True, so the first branch runs.


# 5. COMBINING ALL THREE
print("\n--- Combined Example ---")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful! 🎉")
elif username == "admin" and not (password == "1234"):
    print("Correct username, wrong password.")
else:
    print("Invalid credentials.")


# 6. TRUTH TABLE — what does each operator produce?
print("\n--- Truth Table ---")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and False = {False and False}")
print(f"True  or  False = {True or False}")
print(f"False or  False = {False or False}")
print(f"not True        = {not True}")
print(f"not False       = {not False}")


# 7. TRUTHY & FALSY — Python treats some non-booleans as True/False
print("\n--- Truthy & Falsy ---")
# These are FALSY (act like False):
print(bool(0))       # False — zero
print(bool(""))      # False — empty string
print(bool([]))      # False — empty list
print(bool(None))    # False — the "nothing" value

# Everything else is TRUTHY (acts like True):
print(bool(1))       # True
print(bool("hi"))    # True
print(bool([1,2]))   # True
