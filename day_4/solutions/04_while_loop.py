# ---------------------------------------------------------
# SOLUTION 4: WHILE LOOP 🔁
# ---------------------------------------------------------
import random


# TASK 1: Guess the Number Game.
secret = 42
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == secret:
        print(f"🎉 Got it in {attempts} attempt(s)!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")


# TASK 2: Number Collector — stops on 0 or negative input.
collected = []
while True:
    n = float(input("Enter a positive number (0 or negative to stop): "))
    if n <= 0:
        break
    collected.append(n)

print("Collected:", collected)
if collected:
    print(f"Total: {sum(collected)}")
    print(f"Largest: {max(collected)}")


# TASK 3: Simple ATM with a menu.
balance = 10000
while True:
    print("\n--- ATM Menu ---")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Balance: Rs. {balance}")
    elif choice == "2":
        amount = float(input("Withdraw amount: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"Withdrew Rs. {amount}. New balance: Rs. {balance}")
    elif choice == "3":
        amount = float(input("Deposit amount: "))
        balance += amount
        print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")


# ⭐ BONUS CHALLENGE: Multiplication quiz (5 questions, 2 attempts each).
score = 0
for q in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct = a * b
    for attempt in range(2):
        try:
            answer = int(input(f"What is {a} × {b}? "))
        except ValueError:
            print("Please enter a number.")
            continue
        if answer == correct:
            print("✅ Correct!")
            score += 1
            break
        else:
            if attempt == 0:
                print("❌ Wrong — try once more.")
            else:
                print(f"❌ Out of attempts. Answer was {correct}.")
print(f"\nFinal score: {score}/5")
