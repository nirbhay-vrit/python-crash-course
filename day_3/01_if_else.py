# ---------------------------------------------------------
# DAY 3 | TOPIC 1: IF / ELSE — Making Decisions 🔀
# Python can choose what to do based on a condition!
# ---------------------------------------------------------


# 1. THE IF STATEMENT — only runs if the condition is True
print("--- Basic if ---")
temperature = 35

if temperature > 30:
    print("It's hot outside! Drink water.")

# The indented block ONLY runs when the condition is True.
# If it's False, Python skips it entirely.


# 2. IF / ELSE — choose between two paths
print("\n--- if / else ---")
age = 16

if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote. Come back later.")

# Try changing age to 20 — Python takes the first path.


# 3. REAL EXAMPLE — Password Checker
print("\n--- Password Checker ---")
password = "python123"
correct_password = "python123"

if password == correct_password:
    print("Access granted! Welcome.")
else:
    print("Wrong password. Try again.")


# 4. INDENTATION IS EVERYTHING IN PYTHON!
# Python uses spaces (4 of them) to know what's "inside" the if block.
# Everything indented belongs to that block.

score = 75

if score >= 60:
    print("You passed!")           # inside if — runs when score >= 60
    print("Well done, keep it up") # also inside if — same indented level

print("Exam is over.")             # NOT indented — always runs


# 5. STRINGS CAN BE COMPARED TOO!
print("\n--- String Comparison ---")
name = input("Enter your name: ")

if name == "Alice":
    print("Hello, Alice! You're on the guest list.")
else:
    print(f"Sorry {name}, you're not on the list.")
