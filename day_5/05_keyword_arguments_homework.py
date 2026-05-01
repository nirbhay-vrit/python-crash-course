# ---------------------------------------------------------
# HOMEWORK 5: KEYWORD ARGUMENTS 🏷️
# ---------------------------------------------------------


# TASK 1: Clear Function Calls
# Given this function (don't modify it):
def send_email(to_address, subject, body, priority, attachments):
    print(f"To: {to_address}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Attachments: {attachments}")
    print(f"Body: {body[:30]}...")

# Call it using ONLY keyword arguments in this order:
#   to_address="friend@email.com"
#   subject="Hello!"
#   body="This is a long message..."
#   priority="normal"
#   attachments=False
# Write your code below:





# TASK 2: Book Club Function
# Define a function called 'book_club_signup' with parameters:
#   name (required), book_genre (default "fiction"), meeting_day (default "Saturday")
# Call it three different ways:
#   1. Positional only: ("Alice")
#   2. Mix positional and keyword: ("Bob", meeting_day="Sunday")
#   3. All keywords, any order
# Write your code below:





# TASK 3: Student Record
# Define a function called 'student_record' that takes:
#   name, grade, and any number of extra keyword arguments (**extras)
# Return a dictionary with all the information combined.
# Test it with:
#   student_record("Alice", 10, school="Lincoln High", hobby="painting")
#   student_record("Bob", 9, city="Boston")
# Write your code below:





# TASK 4: Configure Settings
# Define a function called 'configure_app' with:
#   theme (default "light"), notifications (default True), language (default "en")
# Call it to create these configurations:
#   1. All defaults
#   2. Dark theme, Spanish language (keep notifications default)
#   3. Notifications off, keep theme and language default
# Write your code below:





# ⭐ BONUS CHALLENGE:
# Define a function called 'flexible_calculator' that takes:
#   operation ("add", "subtract", "multiply", or "divide")
#   and any number of numbers as keyword arguments (a, b, c, d, etc.)
# Perform the operation on all the numbers provided.
# Example: flexible_calculator("add", a=5, b=3, c=2) → 10
# Write your code below:

