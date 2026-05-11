# ---------------------------------------------------------
# SOLUTION 2: STRINGS 🔤
# ---------------------------------------------------------


# TASK 1: Upper, Lower, Title — string methods all return a NEW string.
full_name = "Bibek Pandey"
print(full_name.upper())   # "BIBEK PANDEY"
print(full_name.lower())   # "bibek pandey"
print(full_name.title())   # "Bibek Pandey"


# TASK 2: String length — len() counts every character (including spaces).
print("My name has " + str(len(full_name)) + " characters!")


# TASK 3: F-string — put the variable name inside {curly braces}.
# F-strings are the cleanest way to mix variables into text.
name = "Bibek"
age = 25
hobby = "Reading"
print(f"Hi! I'm {name}, I'm {age} years old, and I love {hobby}!")


# TASK 4: Name Banner — "=" * 32 repeats the character 32 times.
print("=" * 32)
print(name)
print("=" * 32)


# TASK 5: Input + f-string — input() ALWAYS returns a string.
animal = input("What is your favourite animal? ")
print(f"Wow, {animal} is a great choice! 🐾")


# ⭐ BONUS CHALLENGE:
# .upper() converts to uppercase, then we sandwich it with stars.
typed_name = input("Type your name: ")
print("★★★ " + typed_name.upper() + " ★★★")
