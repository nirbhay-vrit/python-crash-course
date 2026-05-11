# ---------------------------------------------------------
# SOLUTION 1: WHAT IS A FUNCTION? 🧩
# ---------------------------------------------------------
# A function is a reusable block of code:
#   - DEFINE it once with `def`
#   - CALL it many times with `function_name()`


# TASK 1: Define + call your first function.
def introduce_yourself():
    print("Hi, I'm Bibek.")
    print("My favourite subject is Mathematics.")
    print("Fun fact: I once read 50 books in one year!")

introduce_yourself()


# TASK 2: Call the SAME function three times — write the body once, reuse it.
introduce_yourself()
introduce_yourself()
introduce_yourself()


# TASK 3: Drawing function.
def draw_box():
    print("########")
    print("#      #")
    print("########")

draw_box()


# ⭐ BONUS CHALLENGE: Triangle of stars.
def print_triangle():
    for i in range(1, 6):       # 1..5
        print("*" * i)          # repeat the * i times

print_triangle()
