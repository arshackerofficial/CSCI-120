import sys

def calculate_salary_and_bonus(category, hours_worked):
    if category not in {'A', 'M', 'E'}:
        print("Invalid employee category. Please use 'A', 'M', or 'E'.")
        return

    if not hours_worked.isdigit():
        print("Invalid hours worked. Please provide a valid number.")
        return
    hours_worked = int(hours_worked)
    total_salary = 0
    #Write your code here




    #Don't write anything below this line, store the calculated total salary in variable total_salary
    print(f"{total_salary}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <employee_category> <hours_worked>")
    else:
        category = sys.argv[1].upper()
        hours_worked = int(sys.argv[2])
        calculate_salary_and_bonus(category, hours_worked)
