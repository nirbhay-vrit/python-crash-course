# ---------------------------------------------------------
# SOLUTION 2: ELIF — Multiple Choices 🎛️
# ---------------------------------------------------------


# TASK 1: BMI Calculator.
# elif chains are checked top-to-bottom — the FIRST matching branch wins.
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height * height)
print(f"Your BMI is {bmi:.2f}")           # :.2f → 2 decimal places

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight ✅")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# TASK 2: Day Namer.
day_number = int(input("Enter a day number (1–7): "))
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number!")


# TASK 3: Simple Chatbot.
# .lower() makes the check work whether the user types "Happy" or "HAPPY".
feeling = input("How are you feeling today? ").lower()
if feeling == "happy":
    print("Amazing! Keep smiling 😊")
elif feeling == "sad":
    print("I'm sorry. Want to talk about it? 💙")
elif feeling == "tired":
    print("Go rest! Sleep is important 😴")
elif feeling == "hungry":
    print("Go eat something! 🍕")
else:
    print("Interesting! Tell me more.")


# ⭐ BONUS CHALLENGE: Shopping discount.
bill = float(input("Enter your total bill: "))
if bill >= 5000:
    percent = 20
elif bill >= 2000:
    percent = 10
elif bill >= 1000:
    percent = 5
else:
    percent = 0

discount = bill * percent / 100
final_price = bill - discount
print(f"Discount: Rs. {discount:.2f} ({percent}%)")
print(f"Final price: Rs. {final_price:.2f}")
