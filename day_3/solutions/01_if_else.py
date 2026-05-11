# ---------------------------------------------------------
# SOLUTION 1: IF / ELSE — Making Decisions 🔀
# ---------------------------------------------------------


# TASK 1: Temperature Advisor.
# `if / elif / else` lets the program pick ONE branch to run.
temperature = int(input("Enter the current temperature: "))
if temperature > 35:
    print("It's very hot! Stay hydrated. 🥵")
elif temperature >= 20:
    print("Nice weather for a walk! 😊")
else:
    print("It's cold. Wear a jacket! 🧥")


# TASK 2: Even or Odd.
# A number is even when number % 2 leaves NO remainder (== 0).
number = int(input("Enter any whole number: "))
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")


# TASK 3: Guess the Number.
secret = 42
guess = int(input("Guess the secret number: "))
if guess == secret:
    print("🎉 You got it!")
elif guess > secret:
    print("Too high! Try a smaller number.")
else:
    print("Too low! Try a bigger number.")


# ⭐ BONUS CHALLENGE: word length checker.
word = input("Type a word: ")
length = len(word)
if length > 8:
    print("That's a long word!")
elif length == 5:
    print("Perfect 5-letter word!")
else:
    print(f"Your word has {length} letters.")
