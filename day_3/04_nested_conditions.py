# ---------------------------------------------------------
# DAY 3 | TOPIC 4: NESTED CONDITIONS 🪆
# An if inside another if — like boxes within boxes!
# ---------------------------------------------------------


# 1. WHAT IS NESTING?
# You can put an if/elif/else INSIDE another if block.
# Only use nesting when the second question only makes sense
# AFTER the first question is already True.


# 2. CINEMA TICKET SYSTEM
print("--- Cinema Ticket System ---")
age = int(input("Enter your age: "))
has_student_card = input("Do you have a student card? (yes/no): ").lower()

if age >= 5:
    # Old enough to enter — now check what discount applies
    if age < 12:
        print("Child ticket: Rs. 100 🎟️")
    elif age <= 25 and has_student_card == "yes":
        print("Student ticket: Rs. 150 🎟️")
    elif age >= 60:
        print("Senior ticket: Rs. 120 🎟️")
    else:
        print("Adult ticket: Rs. 200 🎟️")
else:
    print("Sorry, children under 5 are not admitted.")


# 3. BANK ATM SIMULATION
print("\n--- ATM Simulation ---")
balance = 5000
pin = "4321"

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("PIN accepted ✅")
    amount = int(input("How much to withdraw? Rs. "))
    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print(f"Insufficient funds. Your balance is Rs. {balance}")
    else:
        balance -= amount   # shorthand for: balance = balance - amount
        print(f"Rs. {amount} dispensed. Remaining balance: Rs. {balance}")
else:
    print("Wrong PIN. Card blocked! 🔒")


# 4. NESTING TIP — too many levels gets messy!
# If you find yourself 3+ levels deep, logical operators (and/or)
# can often flatten your code and make it easier to read.

# MESSY (deep nesting):
# if age >= 18:
#     if has_id:
#         if not is_banned:
#             print("Enter!")

# CLEANER (logical operators):
age = 20
has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print("\nClean version: You may enter!")
