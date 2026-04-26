# ---------------------------------------------------------
# WELCOME TO YOUR FIRST PYTHON SCRIPT!
# ---------------------------------------------------------

# 1. THE PRINT COMMAND
# This tells the computer to show text on the screen.
# Note: Text must always be inside "quotation marks".
print("Hello, Class! Today we are learning Python.")


# 2. PYTHON AS A CALCULATOR
# For math, we don't use quotes. Python just does the work!
print("What is 5 + 5?")
print(5 + 5)

print("What is 100 minus 25?")
print(100 - 25)


# 3. TAKING INPUT (The Interactive Part)
# 'input' lets the user type something. 
# We save that answer in a 'variable' called 'user_name'.
user_name = input("Type your name and press Enter: ")

# Now we use that name in a sentence!
print("It is very nice to meet you, " + user_name + "!")


# 4. THE "WOW" FACTOR: MULTIPLYING TEXT
# In Python, you can actually multiply words. 
# This usually amazes beginners!
print("Let's build a line of rockets...")
print("🚀" * 20)

print("And now, your name 10 times:")
print(user_name * 10)


# 5. MINI GAME: MAD LIBS
# Combining everything to make something fun.
print("\n--- QUICK GAME ---")
color = input("Give me a color: ")
animal = input("Give me an animal: ")

print("Look! A " + color + " " + animal + " is dancing in the classroom!")

