# ---------------------------------------------------------
# DAY 6 | TOPIC 6: PUTTING IT ALL TOGETHER 🏗️
# A mini-project that uses everything from Day 5 & Day 6.
# ---------------------------------------------------------
#
# PROJECT: STUDENT GRADE MANAGER
# We'll build a program that can store students, record their scores,
# calculate stats, and print a full report — all using functions!
#
# Concepts used:
#   ✅ def, parameters, return  (Day 5)
#   ✅ default parameters        (Day 5)
#   ✅ keyword arguments         (Day 5)
#   ✅ multiple return values    (Day 6)
#   ✅ *args                     (Day 6)
#   ✅ **kwargs                  (Day 6)
#   ✅ functions calling functions (Day 6)
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# PART 1: SMALL HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────

def calculate_average(*scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_status(grade):
    if grade in ("A", "B", "C"):
        return "Pass"
    return "Fail"

# Test helpers in isolation first:
print("--- Helper tests ---")
print(calculate_average(80, 90, 70))   # 80.0
print(get_grade(95))                   # A
print(get_grade(55))                   # F
print(get_status("B"))                 # Pass
print(get_status("F"))                 # Fail


# ─────────────────────────────────────────────────────────
# PART 2: BUILDING A STUDENT RECORD
# ─────────────────────────────────────────────────────────
# Returns a dictionary with computed values — uses multiple return
# wrapped in a dict, and **kwargs for optional extras.

def create_student(name, *scores, **extras):
    avg    = calculate_average(*scores)
    grade  = get_grade(avg)
    status = get_status(grade)
    student = {
        "name":    name,
        "scores":  scores,
        "average": avg,
        "grade":   grade,
        "status":  status,
    }
    student.update(extras)   # add any optional info (age, subject, etc.)
    return student

print("\n--- Creating students ---")
alice   = create_student("Alice",   92, 88, 95, 90, age=20, subject="Maths")
bob     = create_student("Bob",     65, 72, 58, 70, age=22)
charlie = create_student("Charlie", 78, 82, 80, 85, subject="Science")

for s in [alice, bob, charlie]:
    print(f"  {s['name']}: avg={s['average']:.1f}, grade={s['grade']}, status={s['status']}")


# ─────────────────────────────────────────────────────────
# PART 3: PRINTING A REPORT CARD
# ─────────────────────────────────────────────────────────

def print_report_card(student, width=38):
    border = "═" * width
    print(f"\n╔{border}╗")
    print(f"║  REPORT CARD{' ' * (width - 13)}║")
    print(f"╠{border}╣")

    print(f"║  Name   : {student['name']:<{width - 11}}║")

    scores_str = ", ".join(str(s) for s in student["scores"])
    print(f"║  Scores : {scores_str:<{width - 11}}║")
    print(f"║  Average: {student['average']:.1f}{' ' * (width - 14)}║")
    print(f"║  Grade  : {student['grade']:<{width - 11}}║")

    status = student["status"]
    status_icon = "🎉" if status == "Pass" else "📚"
    print(f"║  Status : {status} {status_icon}{' ' * (width - 14)}║")

    if "subject" in student:
        print(f"║  Subject: {student['subject']:<{width - 11}}║")

    print(f"╚{border}╝")

print("\n--- Report Cards ---")
print_report_card(alice)
print_report_card(bob)
print_report_card(charlie)


# ─────────────────────────────────────────────────────────
# PART 4: CLASS SUMMARY FUNCTION
# ─────────────────────────────────────────────────────────

def class_summary(students, class_name="Class"):
    averages = [s["average"] for s in students]
    best     = max(students, key=lambda s: s["average"])
    worst    = min(students, key=lambda s: s["average"])
    passing  = [s for s in students if s["status"] == "Pass"]

    class_avg, highest, lowest = (
        sum(averages) / len(averages),
        max(averages),
        min(averages),
    )

    print(f"\n{'─'*38}")
    print(f"  {class_name} Summary")
    print(f"{'─'*38}")
    print(f"  Students     : {len(students)}")
    print(f"  Class avg    : {class_avg:.1f}")
    print(f"  Highest avg  : {highest:.1f} ({best['name']})")
    print(f"  Lowest avg   : {lowest:.1f} ({worst['name']})")
    print(f"  Pass rate    : {len(passing)}/{len(students)}")
    print(f"{'─'*38}")

print("\n--- Class Summary ---")
all_students = [alice, bob, charlie]
class_summary(all_students, class_name="Python Crash Course")


# ─────────────────────────────────────────────────────────
# PART 5: THE DRIVER — RUNNING THE WHOLE PROGRAM
# ─────────────────────────────────────────────────────────

def run():
    students = [
        create_student("Diana", 88, 91, 94, 89, age=21, subject="CS"),
        create_student("Ethan", 55, 60, 58, 63),
        create_student("Fiona", 75, 80, 72, 78, subject="Maths"),
        create_student("George", 95, 98, 100, 97, age=19),
    ]

    print("\n" + "=" * 42)
    print("     FULL STUDENT REPORT")
    print("=" * 42)

    for student in students:
        print_report_card(student)

    class_summary(students, class_name="Advanced Python")

print("\n\n--- Running the full program ---")
run()
