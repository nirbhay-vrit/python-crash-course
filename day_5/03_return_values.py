# ---------------------------------------------------------
# DAY 5 | TOPIC 3: RETURN VALUES — Getting Data BACK 📤
# A function can GIVE YOU BACK a result using 'return'!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM — FUNCTIONS THAT ONLY PRINT
# ─────────────────────────────────────────────────────────
# So far our functions just print things.
# But what if you want to USE the result in your code?

def add_numbers_print(a, b):
    print(a + b)       # just prints — result disappears!

add_numbers_print(3, 5)

# Can we store the result? Let's try:
result = add_numbers_print(10, 20)
print(result)          # prints None! The function gave back nothing.


# ─────────────────────────────────────────────────────────
# SECTION 2: THE 'return' KEYWORD
# ─────────────────────────────────────────────────────────
# Use 'return' to SEND a value back to whoever called the function.
# After return, the function stops immediately.

def add_numbers(a, b):
    total = a + b
    return total       # ← sends 'total' back

print("\n--- Using return ---")
answer = add_numbers(3, 5)    # store the returned value
print(answer)                 # 8

bigger = add_numbers(100, 200)
print(bigger)                 # 300


# ─────────────────────────────────────────────────────────
# SECTION 3: USING THE RETURNED VALUE DIRECTLY
# ─────────────────────────────────────────────────────────
# You don't have to store it in a variable first.
# You can use the returned value directly!

print("\n--- Using return value directly ---")
print(add_numbers(7, 3))                    # 10
print("Sum:", add_numbers(50, 50))          # Sum: 100
print(add_numbers(1, 1) + add_numbers(2, 2))  # 3 + 4 = 7


# ─────────────────────────────────────────────────────────
# SECTION 4: RETURN STOPS THE FUNCTION
# ─────────────────────────────────────────────────────────
# As soon as Python hits 'return', the function ends.
# Any code AFTER return is never reached.

def first_positive(numbers):
    for n in numbers:
        if n > 0:
            return n    # ← returns immediately when found!
    # If no positive number is found, Python returns None automatically.

print("\n--- return exits early ---")
result = first_positive([-3, -1, 7, 10, 2])
print(result)    # 7  (stops as soon as it finds 7)


# ─────────────────────────────────────────────────────────
# SECTION 5: RETURN A CALCULATION DIRECTLY
# ─────────────────────────────────────────────────────────
# You don't need a variable inside — you can return an expression!

def square(n):
    return n * n

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print("\n--- Returning expressions ---")
print(square(4))                        # 16
print(square(9))                        # 81
print(celsius_to_fahrenheit(0))         # 32.0
print(celsius_to_fahrenheit(100))       # 212.0
