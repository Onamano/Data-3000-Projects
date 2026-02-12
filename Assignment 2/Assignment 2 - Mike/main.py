# Importing the functions from the other files within the program to allow their use when called, as well as the time library
import time
from tkinter import *
import tkinter.messagebox
from employee import Employee
from selection_sort import selection_sort_by_salary
from quick_sort import quick_sort_by_name
from binary_search import binary_search_by_name

# Function for reading the input file and adding the users and attributes to an array as objects
# Allows for error handliing within the try/except block
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
    except TypeError:
        print("Unable to find file, please check filepath")

# Function which writes the list when it's sorted by salary into new .csv files, using attributes from objects 
def write_employees_to_file(filename, employees):
    with open(filename, "w") as file:
        for e in employees:
            salary = e.calc_hourly_salary()

            #TEMP DEBUG PRINT
            #print(e.name, salary)

            file.write(
                f"{e.emp_id},{e.name},{e.hours_worked},{e.hourly_rate:.2f},"
                f"{e.deduction_province},{e.deduction_federal},{e.education_allowance},"
                f"{salary}\n"

            )

# Main function
def main():
    filename = input("\nEnter the employee data file path ◄► ") # DATA-3000\Assignments\Assignment 2\employeesWithoutRepeat.txt 
    print("Read employee data data from file ", filename)
    employees = read_employees_from_file(filename)


    #Selection Sort (Sorted by Salary)
    salary_list = employees.copy()

    # Timing how long it takes for the list to be sorted by salary using the selection sort method
    start = time.time()
    selection_sort_by_salary(salary_list)
    end = time.time()

    # Printing runtime and writing the sorted list to a new file
    print(" ")
    print(" The Performance of our Sorting Algorithms")
    print("###########################################")
    print(f"Selection Sort Time ► {int((end - start) * 1000)} ms")
    write_employees_to_file("sortedemployeeBySalary.csv", salary_list)
    

    # Quick Sort (Sorted by Name)
    name_list = employees.copy()

    # Timing how long it takes for the list to be sorted by name using the quick sort method
    start = time.time()
    quick_sort_by_name(name_list, 0, len(name_list) - 1)
    #time.sleep(1) # Added a sleep timer as the quick sort was running in less than 1 ms - see about changing to micro-/nanoseconds
    end = time.time()

    # Prints the runtime to the console and writes the sorted list to a new file
    print(f"Quick Sort Time ► {int((end - start) * 1000)} ms")
    print("###########################################")
    print(" ")
    write_employees_to_file("sortedemployeeByName.csv", name_list)

    # Printing to console informing user that files are being written
    print("Writing employee data sorted by their hourly salaries into file ◄►")
    print("Writing employee data sorted by their names into file ◄►")
    print(" ")

    # Binary Search for employee names
    target = input("Enter the name of the employee to search ◄► ")
    index = binary_search_by_name(name_list, target, 0, len(name_list) - 1)

    # Prints the employees index number to the console, if the function returns -1 it prints "Employee not found"
    if index != -1:
        print(" ")
        print(f"Employee found at index ◄► {index}")
        print(" ")
    else:
        print("Employee not found")
        print(" ")


# Run main()
if __name__ == "__main__":
    # Creates a pop-up window which needs to be clicked before the program can run
    popUp = Tk()
    popUp.wm_withdraw()
    popUp.geometry("1x1+200+200")  # Positioning at x:200,y:200
    tkinter.messagebox.showinfo(title="Start", message="Employee Searching and Sorting Program!\n\n Press OK to Start")

    # Run the main function
    main()



# References
# [1] https://sqlpey.com/python/top-12-ways-to-create-a-simple-message-box-in-python/ - tkinter message boxes