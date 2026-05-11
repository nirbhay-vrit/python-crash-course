# ---------------------------------------------------------
# SOLUTION 5: KEYWORD ARGUMENTS 🏷️
# ---------------------------------------------------------
# Keyword arguments let you pass values BY NAME, in any order.
# Much clearer than positional arguments when there are many parameters.


# TASK 1: Clear function calls — all keyword arguments.
def send_email(to_address, subject, body, priority, attachments):
    print(f"To: {to_address}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Attachments: {attachments}")
    print(f"Body: {body[:30]}...")

send_email(
    to_address="friend@email.com",
    subject="Hello!",
    body="This is a long message that contains lots of text to demo slicing.",
    priority="normal",
    attachments=False,
)


# TASK 2: Book club signup — three call styles.
def book_club_signup(name, book_genre="fiction", meeting_day="Saturday"):
    print(f"{name} signed up for {book_genre} on {meeting_day}")

book_club_signup("Alice")                                    # positional only
book_club_signup("Bob", meeting_day="Sunday")                # mix
book_club_signup(book_genre="mystery", name="Carol",         # all keyword, any order
                 meeting_day="Friday")


# TASK 3: Student record — capture extras with **kwargs.
def student_record(name, grade, **extras):
    record = {"name": name, "grade": grade}
    record.update(extras)       # merge the keyword extras into the dict
    return record

print(student_record("Alice", 10, school="Lincoln High", hobby="painting"))
print(student_record("Bob", 9, city="Boston"))


# TASK 4: Configure settings.
def configure_app(theme="light", notifications=True, language="en"):
    return {"theme": theme, "notifications": notifications, "language": language}

print(configure_app())                                       # all defaults
print(configure_app(theme="dark", language="es"))            # dark + Spanish
print(configure_app(notifications=False))                    # only notifications off


# ⭐ BONUS CHALLENGE: Flexible calculator with kwargs.
def flexible_calculator(operation, **numbers):
    values = list(numbers.values())
    if not values:
        return 0

    if operation == "add":
        return sum(values)
    if operation == "subtract":
        # Start from the first value, subtract the rest.
        result = values[0]
        for v in values[1:]:
            result -= v
        return result
    if operation == "multiply":
        result = 1
        for v in values:
            result *= v
        return result
    if operation == "divide":
        result = values[0]
        for v in values[1:]:
            if v == 0:
                return "Cannot divide by zero!"
            result /= v
        return result
    return "Unknown operation"

print(flexible_calculator("add", a=5, b=3, c=2))             # 10
print(flexible_calculator("multiply", a=2, b=3, c=4))        # 24
print(flexible_calculator("subtract", a=100, b=30, c=20))    # 50
print(flexible_calculator("divide", a=100, b=2, c=5))        # 10.0
