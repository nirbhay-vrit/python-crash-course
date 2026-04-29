# ---------------------------------------------------------
# DAY 3 | TOPIC 5: LOOPS — Doing Things Repeatedly 🔄
# Instead of copy-pasting, let Python repeat for you!
# ---------------------------------------------------------


# 1. THE FOR LOOP — loop over a sequence
print("--- for loop over a list ---")
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(f"I love {fruit}!")

# Python takes each item from the list, puts it in 'fruit',
# runs the indented block, then moves to the next item.


# 2. FOR LOOP WITH range() — loop a fixed number of times
print("\n--- for loop with range() ---")
for i in range(5):          # 0, 1, 2, 3, 4
    print(f"Count: {i}")

print("\n--- range(1, 6) ---")
for i in range(1, 6):       # 1, 2, 3, 4, 5  (stop is not included!)
    print(f"Step {i}")

print("\n--- range(0, 11, 2) ---")
for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10  (step of 2)
    print(i, end=" ")
print()


# 3. WHILE LOOP — loop as long as a condition is True
print("\n--- while loop ---")
countdown = 5

while countdown > 0:
    print(f"T minus {countdown}...")
    countdown -= 1     # countdown = countdown - 1

print("Liftoff! 🚀")

# WARNING: make sure the condition eventually becomes False
# or your loop will run forever! (press Ctrl+C to stop)


# 4. BREAK — exit a loop early
print("\n--- break ---")
for number in range(1, 11):
    if number == 5:
        print("Found 5! Stopping early.")
        break            # jump OUT of the loop immediately
    print(number)


# 5. PRACTICAL: Sum all numbers in a list using a for loop
print("\n--- Calculating total ---")
prices = [120, 250, 75, 340, 99]
total = 0

for price in prices:
    total += price     # total = total + price

print(f"Items: {prices}")
print(f"Total: Rs. {total}")
