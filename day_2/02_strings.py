# ---------------------------------------------------------
# DAY 2 | TOPIC 2: STRINGS 🔤
# A string is any text — letters, words, sentences, emojis!
# ---------------------------------------------------------


# 1. WHAT IS A STRING?
# Anything inside quotes (" " or ' ') is a string.
greeting = "Hello, World!"
single_quote_version = 'This works too!'
with_emoji = "Python is absolutely 🔥"

print(greeting)
print(single_quote_version)
print(with_emoji)


# 2. COMBINING STRINGS (Concatenation)
# Use + to glue two strings together.
first_part = "Python"
second_part = " is awesome!"
full_sentence = first_part + second_part
print(full_sentence)

# You can chain as many as you like:
print("I" + " " + "love" + " " + "coding!")


# 3. REPEATING STRINGS
# Use * to repeat a string multiple times.
print("\n" + "⭐" * 30)
print("Ha" * 6 + "!")
print("=" * 30)


# 4. STRING LENGTH
# len() counts every single character (including spaces!).
city = "Kathmandu"
print("\nThe word:", city)
print("Number of characters:", len(city))
print("Does 'Hi' have 2 characters?", len("Hi") == 2)


# 5. CHANGING CASE
name = "alice in wonderland"
print("\nOriginal :", name)
print("UPPERCASE:", name.upper())
print("lowercase:", name.lower())
print("Title Case:", name.title())  # Capitalises Every First Letter


# 6. F-STRINGS — The Clean, Modern Way ⭐
# Put f before the quote, then use {} to drop variables right in.
student_name = "Bob"
student_age = 17

# Old way (messy with lots of + signs):
print("\nOld way: " + "My name is " + student_name + " and I am " + str(student_age) + ".")

# F-string way (so much cleaner!):
print(f"F-string: My name is {student_name} and I am {student_age}.")

# You can even do MATHS inside the curly braces:
print(f"Next year I will be {student_age + 1} years old!")


# 7. GETTING INPUT FROM THE USER
print("\n--- Let's try f-strings live! ---")
user_name = input("What is your name? ")
user_city = input("Which city are you from? ")

print(f"\nHello, {user_name} from {user_city}! Welcome to Python! 🎉")
print(f"Your name has {len(user_name)} characters.")

