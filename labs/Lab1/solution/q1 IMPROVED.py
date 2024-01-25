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
    
    hourly_rates = {'A': 25, 'M': 40, 'E': 75}
    overtime_rate_increase = {'A': 5, 'M': 10, 'E': 25}
    bonus_ranges = (40, 50, 60)
    bonus_rates = {'A': 100, 'M': 150, 'E': 250}

    base_rate = hourly_rates[category]
    overtime_rate = base_rate + overtime_rate_increase[category]
    
    # Calculate salary based on hours worked
    if hours_worked <= 40:
        salary = hours_worked * base_rate
    else:
        salary = 40 * base_rate + (hours_worked - 40) * overtime_rate

    # Calculate bonus based on hours worked
    if bonus_ranges[0] < hours_worked <= bonus_ranges[1]:
        bonus = bonus_rates[category]
    elif bonus_ranges[1] < hours_worked <= bonus_ranges[2]:
        bonus = 2 * bonus_rates[category]  # Double the bonus

    total_salary = salary + bonus

    #Don't write anything below this line, store the calculated total salary in variable total_salary
    print(f"{total_salary}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <employee_category> <hours_worked>")
    else:
        category = sys.argv[1].upper()
        hours_worked = int(sys.argv[2])
        calculate_salary_and_bonus(category, hours_worked)
