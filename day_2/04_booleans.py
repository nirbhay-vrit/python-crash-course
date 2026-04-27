# ---------------------------------------------------------
# DAY 2 | TOPIC 4: BOOLEANS, type(), AND TYPE CONVERSION ✅❌
# Booleans are the simplest data type: only True or False!
# ---------------------------------------------------------


# 1. BOOLEAN VALUES
is_raining = False
has_homework = True
is_python_fun = True
is_monday = False

print("Is it raining?     ", is_raining)
print("Is there homework? ", has_homework)
print("Is Python fun?     ", is_python_fun)
print("Is it Monday?      ", is_monday)


# 2. COMPARISON OPERATORS — these PRODUCE True or False
x = 10
y = 20

print(f"\n--- Comparing {x} and {y} ---")
print(f"{x} == {y}  →  {x == y}")    # equal to
print(f"{x} != {y}  →  {x != y}")    # NOT equal to
print(f"{x} >  {y}  →  {x > y}")     # greater than
print(f"{x} <  {y}  →  {x < y}")     # less than
print(f"{x} >= {y}  →  {x >= y}")    # greater than OR equal
print(f"{x} <= {y}  →  {x <= y}")    # less than OR equal


# 3. THE type() DETECTIVE
# Not sure what data type a value is? Just ask Python!
print("\n--- Checking Data Types ---")
print(type("Hello"))         # <class 'str'>
print(type(42))              # <class 'int'>
print(type(3.14))            # <class 'float'>
print(type(True))            # <class 'bool'>
print(type(is_raining))      # <class 'bool'>  ← variable works too!


# 4. TYPE CONVERSION (a.k.a. "Casting")
# You can change a value from one type to another.
age_as_text = "25"                # This is a STRING — you cannot do math with it!
age_as_number = int(age_as_text)  # Now it's an INTEGER — ready for maths!

print("\n--- Type Conversion ---")
print(f"Before: '{age_as_text}'  → type: {type(age_as_text)}")
print(f"After:  {age_as_number}  → type: {type(age_as_number)}")

# All the common conversions:
print("\n--- Conversion Cheat-Sheet ---")
print(int("100"))           # str  → int   : 100
print(float("3.14"))        # str  → float : 3.14
print(str(42))              # int  → str   : "42"
print(bool(1))              # int  → bool  : True
print(bool(0))              # 0 is ALWAYS False — remember this!


# 5. WHY THIS MATTERS: input() ALWAYS returns a string!
print("\n--- The input() Trap (and how to escape it!) ---")
raw = input("Enter a number: ")
print(f"What Python sees: '{raw}'  —  type: {type(raw)}")

# Converting lets us do real maths:
number = int(raw)
print(f"After int():  {number}  +  10  =  {number + 10}")
