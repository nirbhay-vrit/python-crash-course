# ---------------------------------------------------------
# SOLUTION 4: NESTED CONDITIONS 🪆
# ---------------------------------------------------------
# A nested condition is an if/else INSIDE another if/else.


# TASK 1: Concert Ticket Pricing.
age = int(input("Your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if age < 5:
    print("Not admitted (too young).")
elif age <= 12:
    print("Child ticket: Rs. 200")
elif age <= 17:
    # Nested branch — first we know they're a teen, THEN we check membership.
    if is_member:
        print("Teen ticket (member): Rs. 250")
    else:
        print("Teen ticket: Rs. 350")
else:
    if is_member:
        print("Adult ticket (member): Rs. 400")
    else:
        print("Adult ticket: Rs. 500")


# TASK 2: Login System with Role.
admin = {"username": "admin", "password": "pass123", "role": "superuser"}
user1 = {"username": "user1", "password": "abc", "role": "viewer"}

entered_user = input("Username: ")
entered_pass = input("Password: ")

if entered_user == admin["username"] and entered_pass == admin["password"]:
    print("Welcome, Superuser! You have full access.")
elif entered_user == user1["username"] and entered_pass == user1["password"]:
    print("Welcome, user1! You have view-only access.")
else:
    print("Access denied.")


# ⭐ BONUS CHALLENGE: Quiz game (3 questions, 1 point each).
score = 0

a1 = input("1. What is 5 + 7? ")
if a1 == "12":
    score += 1

a2 = input("2. What is the capital of Nepal? ").lower()
if a2 == "kathmandu":
    score += 1

a3 = input("3. What language are we learning? ").lower()
if a3 == "python":
    score += 1

print(f"\nYou scored {score}/3")
if score == 3:
    print("Perfect score! 🌟")
elif score == 2:
    print("Great job! Almost there.")
elif score == 1:
    print("Good try. Keep studying!")
else:
    print("Better luck next time! 📚")
