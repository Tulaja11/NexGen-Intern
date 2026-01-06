# ================================
# Student Report Card System
# ================================
 
import re

# ------------------------
# Student Class
# ------------------------
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks  # List of 3 subject marks
    
    def get_average(self):
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self):
        return "Pass" if self.get_average() >= 40 else "Fail"


# ------------------------
# Helper Functions
# ------------------------

def display_table(students, title="Student Records"):
    """Prints a list of students in table format with borders"""
    print(f"\n===== {title} =====")
    print("+------+--------------+----------------------+-----------+--------+")
    print("| Roll | Name         | Marks                | Average   | Result |")
    print("+------+--------------+----------------------+-----------+--------+")
    for s in students:
        marks_str = ", ".join(map(str, s.marks))
        print(f"| {s.roll:<4} | {s.name:<12} | {marks_str:<20} | {s.get_average():<9.2f} | {s.get_grade():<6} |")
        print("+------+--------------+----------------------+-----------+--------+")

def print_report_card(s):
    """Shows single student report card in bordered vertical format"""
    print("\n----- Report Card -----")
    print("+------------+------------------+")
    print(f"| Roll No    | {s.roll:<16}|")
    print("+------------+------------------+")
    print(f"| Name       | {s.name:<16}|")
    print("+------------+------------------+")
    for i, mark in enumerate(s.marks, 1):
        print(f"| Subject {i}  | {mark:<16}|")
        print("+------------+------------------+")
    print(f"| Average    | {s.get_average():<16.2f}|")
    print("+------------+------------------+")
    print(f"| Result     | {s.get_grade():<16}|")
    print("+------------+------------------+")

def find_topper(students):
    topper = max(students, key=lambda s: s.get_average())
    display_table([topper], "Topper")

def show_leaderboard(students):
    """Top 3 students in bordered table format"""
    top_three = sorted(students, key=lambda s: s.get_average(), reverse=True)[:3]
    print("\n=== Leaderboard (Top 3 Students) ===")
    print("+------+--------------+-----------+")
    print("| Rank | Name         | Average   |")
    print("+------+--------------+-----------+")
    for i, s in enumerate(top_three, 1):
        print(f"| {i:<4} | {s.name:<12} | {s.get_average():<9.2f}|")
        print("+------+--------------+-----------+")

def search_by_roll(students):
    try:
        roll = int(input("Enter roll number to search: "))
        found = next((s for s in students if s.roll == roll), None)
        if found:
            print_report_card(found)
        else:
            print("Student not found.")
    except ValueError:
        print("Enter a valid roll number.")

def search_by_name(students):
    name_part = input("Enter part of name to search: ").lower()
    matches = [s for s in students if name_part in s.name.lower()]
    if matches:
        display_table(matches, f"Search Results for '{name_part}'")
    else:
        print("No matching student found.")

def sort_students(students):
    order = input("Sort ascending or descending? (a/d): ").lower()
    reverse = True if order == 'd' else False
    sorted_list = sorted(students, key=lambda s: s.get_average(), reverse=reverse)
    display_table(sorted_list, "Sorted Students")

def show_pass_fail(students):
    passed = [s for s in students if s.get_grade() == "Pass"]
    failed = [s for s in students if s.get_grade() == "Fail"]
    display_table(passed, "Passed Students")
    display_table(failed, "Failed Students")

def factorial_demo():
    try:
        num = int(input("Enter a roll number to find factorial: "))
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n-1)
        print(f"\nFactorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid number.")


# ------------------------
# Main Menu
# ------------------------
def main():
    students = [
        Student(20, "Aadi", [85, 90, 88]),
        Student(21, "Banti", [30, 21, 40]),
        Student(22, "Cherry", [70, 65, 72]),
        Student(23, "Deepa", [30, 28, 35]),
        Student(24, "Elisha",[42, 36, 78])
    ]

    while True:
        print("\n=== Student Report Card System ===")
        print("1. Display All Students")
        print("2. Print Report Card by Roll")
        print("3. Search Students by Name")
        print("4. Find Topper")
        print("5. Show Leaderboard (Top 3)")
        print("6. Sort Students by Average")
        print("7. Show Pass/Fail Lists")
        print("8. Factorial of Roll Number (Recursion Demo)")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_table(students)
        elif choice == '2':
            search_by_roll(students)
        elif choice == '3':
            search_by_name(students)
        elif choice == '4':
            find_topper(students)
        elif choice == '5':
            show_leaderboard(students)
        elif choice == '6':
            sort_students(students)
        elif choice == '7':
            show_pass_fail(students)
        elif choice == '8':
            factorial_demo()
        elif choice == '9':
            print("Exiting program.......... Goodbye !")
            continue   # keeps looping (unique touch)
        else:
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()
