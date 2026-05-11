# ---------------------------------------------------------
# SOLUTION 5: LOOPS — for & while 🔄
# ---------------------------------------------------------


# TASK 1: Multiplication Table.
# range(1, 11) gives 1, 2, 3, ... 10 (the END value is excluded).
number = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# TASK 2: Sum of even numbers from 1 to 50.
# Pattern: start total at 0, add each matching number.
total = 0
for n in range(1, 51):
    if n % 2 == 0:
        total += n              # shortcut for: total = total + n
print(f"Sum of even numbers 1–50: {total}")


# TASK 3: Password Retry — while loops repeat WHILE a condition is True.
password = "letmein"
attempts = 0
max_attempts = 3
granted = False

while attempts < max_attempts:
    entered = input("Enter password: ")
    attempts += 1
    if entered == password:
        granted = True
        break                   # leave the loop immediately on success
    else:
        remaining = max_attempts - attempts
        print(f"Wrong! Attempts left: {remaining}")

if granted:
    print("Access granted! 🎉")
else:
    print("Account locked! 🔒")


# ⭐ BONUS CHALLENGE: Number collector until "done".
numbers = []
while True:                     # "infinite" loop — we exit with break
    entry = input("Enter a number (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    numbers.append(float(entry))

count = len(numbers)
print(f"Count: {count}")
if count > 0:
    total = sum(numbers)
    print(f"Sum: {total}")
    print(f"Average: {total / count}")
else:
    print("No numbers entered.")
