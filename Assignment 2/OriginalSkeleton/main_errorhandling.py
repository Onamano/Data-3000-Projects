#main.py

#Imports for Class and sort/search methods
import time
from employee import Employee
from selection_sort import selection_sort_by_salary
from quick_sort import quick_sort_by_name
from binary_search import binary_search_by_name

#Reads employee data from text file into employees list
def read_employees_from_file(filename):
    employees = []
    try:
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

    except FileNotFoundError:
        print(f"File at {filename} was not found")
    except OSError:
        print(f"Error occurred while attempting to read file")

#Writes to file using the employees list
def write_employees_to_file(filename, employees):
    try:
        with open(filename, "w") as file:
            for e in employees:
                salary = e.calc_hourly_salary()

                file.write(
                    f"{e.emp_id},{e.name},{e.hours_worked},{e.hourly_rate},"
                    f"{e.deduction_province},{e.deduction_federal},{e.education_allowance},"
                    f"{salary}\n"

                )
    except FileNotFoundError:
        print(f"File at {filename} was not found")

def main():
    filename = input("Enter the employee data file path - ")

    employees = read_employees_from_file(filename)

    try:
        #Copies employees list to salary_list for selection sort and writing to .csv
        salary_list = employees.copy() #AttributeError if initial file path is incorrect/file does not exist
        
        #Selection sort (by salary)
        start = time.time()
        selection_sort_by_salary(salary_list)
        end = time.time()
        print(f"Selection Sort Time - {int((end - start) * 1000)} ms")

        #Writes from sorted salary_list into .csv file
        write_employees_to_file("sortedemployeeBySalary.csv", salary_list)
    except AttributeError:
        print("Unable to generate salary_list to perform selection sort")


    try:
        #Copies employees list to name_list for quick sort and writing to .csv
        name_list = employees.copy() #AttributeError if initial file path is incorrect/file does not exist

        #Quick sort (by name)
        start = time.time()
        quick_sort_by_name(name_list, 0, len(name_list) - 1)
        end = time.time()
        print(f"Quick Sort Time - {int((end - start) * 1000)} ms")

        #Writes from sorted name_list into .csv file
        write_employees_to_file("sortedemployeeByName.csv", name_list)
    except AttributeError:
        print("Unable to generate name_list to perform quick sort")


    try:
        #Binary search using previously generated name_list
        target = input("Enter the name of the employee to search - ")
        index = binary_search_by_name(name_list, target, 0, len(name_list) - 1)

        if index != -1:
            print(f"Employee found at index - {index}")
        else:
            print("Employee not found")
    except UnboundLocalError:
        print("Unable to perform binary search on empty list")



if __name__ == "__main__":
    main()
