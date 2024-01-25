#815805

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
    bonus = 0
    if(category == "A"):
        if(hours_worked > 40 and hours_worked <= 50):
            bonus = 100
        elif(hours_worked > 50 and hours_worked <= 60):
            bonus = 200
        for i in range(hours_worked):
            if (i+1) > 40:
                total_salary = total_salary + 30
            else:
                total_salary = total_salary + 25
    elif(category == "M"):
        if(hours_worked > 40 and hours_worked <= 50):
            bonus = 150
        elif(hours_worked > 50 and hours_worked <= 60):
            bonus = 300
        for i in range(hours_worked):
            if (i+1) > 40:
                total_salary = total_salary + 50
            else:
                total_salary = total_salary + 40
    elif(category == "E"):
        if(hours_worked > 40 and hours_worked <= 50):
            bonus = 250
        elif(hours_worked > 50 and hours_worked <= 60):
            bonus = 500
        for i in range(hours_worked):
            if (i+1) > 40:
                total_salary = total_salary + 100
            else:
                total_salary = total_salary + 75
                
    total_salary = total_salary+bonus   



    #Don't write anything below this line, store the calculated total salary in variable total_salary
    print(f"{total_salary}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <employee_category> <hours_worked>")
    else:
        category = sys.argv[1].upper()
        hours_worked = int(sys.argv[2])
        calculate_salary_and_bonus(category, hours_worked)
