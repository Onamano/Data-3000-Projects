#main.py

import time
from employee import Employee
from selection_sort import selection_sort_by_salary
from quick_sort import quick_sort_by_name
from binary_search import binary_search_by_name

def read_employees_from_file(filename):
    employees = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")

            emp = Employee(
                int(parts[0]),
                parts[1],
                float(parts[2]),
                float(parts[3]),
                float(parts[4]),
                float(parts[5]),
                float(parts[6])
            )

            employees.append(emp)

    return employees

def write_employees_to_file(filename, employees):
    with open(filename, "w") as file:
        for e in employees:
            salary = e.calc_hourly_salary()

            #TEMP DEBUG PRINT
            #print(e.name, salary)

            file.write(
                f"{e.emp_id},{e.name},{e.hours_worked},{e.hourly_rate},"
                f"{e.deduction_province},{e.deduction_federal},{e.education_allowance},"
                f"{salary}\n"

            )

def main():
    filename = input("Enter the employee data file path - ")

    employees = read_employees_from_file(filename)

    #selection sort (by salary)
    salary_list = employees.copy()

    start = time.time()
    selection_sort_by_salary(salary_list)
    end = time.time()

    print(f"Selection Sort Time - {int((end - start) * 1000)} ms")
    write_employees_to_file("sortedemployeeBySalary.csv", salary_list)
    
    #quick sort (by name)
    name_list = employees.copy()

    start = time.time()
    quick_sort_by_name(name_list, 0, len(name_list) - 1)
    #time.sleep(1)
    end = time.time()

    print(f"Quick Sort Time - {int((end - start) * 1000)} ms")
    write_employees_to_file("sortedemployeeByName.csv", name_list)

    #binary search
    target = input("Enter the name of the employee to search - ")
    index = binary_search_by_name(name_list, target, 0, len(name_list) - 1)

    if index != -1:
        print(f"Employee found at index - {index}")
    else:
        print("Employee not found")


if __name__ == "__main__":
    main()
