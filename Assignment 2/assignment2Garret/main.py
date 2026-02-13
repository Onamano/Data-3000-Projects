#main.py

#importing tkinter module for the GUI popup prompting to start the program.
import tkinter as tk
from tkinter import messagebox

#importing time module to measure performance of sorting algorithms 
import time

#importing the employee class and custom functions for sorting and searching
#these are defined in separate files for organization
from employee import Employee
from selection_sort import selection_sort_by_salary
from quick_sort import quick_sort_by_name
from binary_search import binary_search_by_name

#function that reads employee data from a csv file, and returns a list of Employee objects, expects the location of the file to be passed to it
def read_employees_from_file(filename):
    employees = [] #list to store Employee objects

    try:
        #open the file in read mode. filename is the path provided by the user in main()
        with open(filename, "r") as file:
            #loop thorugh each line in the file. 
            #enumerate() gives us a tuple (line_number, line), starting at 1 so errors can include the index of the line where an error occured 
            for line_number, line in enumerate(file, start=1): #gives us a tuple in the form (index, value) so if a line has an error in the data, we can get the index number and include it in the error message
                line = line.strip() #remove any leading or trailing whitespace
                if line == "": #skip any empty lines if there are any
                    continue

                try:
                    #split each line by commas into a list of values for that employee
                    #each line in the CSV corresponds to one employee, so this gives us a list like:
                    #[ID, Name HoursWorked, HourlyRate, DeductionProvince, DeductionFederal, EducationAllowance]
                    #this list is then used to create an Employee object for that line
                    employee_data = line.split(",")
                    if len(employee_data) !=7: #check to make sure there are exactly 7 fields for each employees data
                        print(f"Skipping line {line_number}: invalid format") #otherwise print this and skip this line
                        continue

                    #create an eemployee object for each line read from the CSV
                    #convert appropriate fields into ints or floats
                    #they would all be read as strings from the CSV if i did not specify, and we cant perform calculations on strings
                    employee = Employee(  
                        int(employee_data[0]),      #employee ID
                        employee_data[1],           #name
                        float(employee_data[2]),    #hours worked
                        float(employee_data[3]),    #hourly rate
                        float(employee_data[4]),    #provincial deduction
                        float(employee_data[5]),    #federal deduction
                        float(employee_data[6])     #education allowance
                    )
                    employees.append(employee) #add each employee objects to the employees list

                except ValueError: #if a conversion to int or float fails, skip this line and show this message, with the line_number(index) of where it occured specified
                    print(f"Skipping line {line_number}: invalid data")
        
    except FileNotFoundError: #for if the file path is invalid or file doesnt exist
        print (f"Error: File '{filename}' not found")
        return [] #return empty list so program doesnt crash later on 
    except IOError: #catch other file read errors (such as permissions)
        print(f"Error: Could not read file '{filename}'.")
        return []
    return employees #returns list of employee objects back to main()

#function that writes employee data to CSV file 
# it expects a location of the output file and the list of employee objects to be written to the file
def write_employees_to_file(filename, employees):
    try:
        #open the output file in write mode. will create file if it doesnt exist
        #or overwrite it if it already exists
        with open(filename, "w") as file:
            for e in employees:                    #loop thorugh each employee object in the employees list
                salary = e.calc_hourly_salary()    #calculate the salary for this employee object and store in salary variable

                #write employee data to the CSV file
                #format numbers to 2 decimal places
                file.write(
                    f"{e.emp_id},{e.name},{e.hours_worked:.2f},{e.hourly_rate:.2f},"
                    f"{e.deduction_province:.2f},{e.deduction_federal:.2f},{e.education_allowance:.2f},"
                    f"{salary:.2f}\n"
                )
    except IOError: #catch any errors while writing the file
        print(f"Error: Could not write to file '{filename}'.")

#defining the main function that runs when the program is launched
def main():

    #this creates a hidden tkinter root window for the initial popup
    popup = tk.Tk()
    popup.withdraw() #this hides the main tkinter window because we only want the popup

    #shows a message box with OK button, trying to replicate java joptionpane behavior 
    #program will pause here until the user selects OK
    messagebox.showinfo("Employee Data Sorting and Searching Program!", "Press OK to Start")

    popup.destroy() #destroy the hidden root window now that the popup is done

    #prompt user for full path to the CSV employee file
    filename = input("Enter the employee data file path - ")
    print(f"Read employee data from file {filename}\n")

    #calls read_employees_from_file function and passes the path of the CSV file to it
    #read_employees_from_file will return a list of Employee objects which are stored in this employees variable
    employees = read_employees_from_file(filename)

    #-------------------------
    #selection sort by salary
    #------------------------

    #create a copy of the list of employee objects and store it in this salary_list variable
    salary_list = employees.copy()

    start = time.time() #record start time to measure performance 
    selection_sort_by_salary(salary_list) #call this function, passing the salary_list of employee objects to it
    end = time.time() #record end time after sorting

    print("The performance of our sorting algorithms")
    print("#########################################")
    #print how long sorting took in milliseconds (thats why we multiplied by 1000 here because originally output would be in seconds), we specify int so it does not output as a float and look messy
    print(f"Selection Sort Time - {int((end - start) * 1000)} ms")

    #call this function passing the location of the output file to it, as well as the list thats been sorted by salary, this now sorted list of employee objects will be written to the csv file
    write_employees_to_file("output/sortedemployeeBySalary.csv", salary_list)
    
    #-------------------
    #quick sort by name
    #-------------------
    name_list = employees.copy() #make a copy of the original employees list of employee objects

    start = time.time() #recording the start time 
    quick_sort_by_name(name_list, 0, len(name_list) - 1) #call the quick_sort_by_name function and pass it the new list of unsorted employee objects (name_list), the first index(low) and last index(high) 
    end = time.time() #record the end time

    print(f"Quick Sort Time - {int((end - start) * 1000)} ms") #subtract start time from end time and multiply by 1000 to get time in ms specifying int because its cleaner looking than float
    print("#########################################\n")
    write_employees_to_file("output/sortedemployeeByName.csv", name_list) #call this function to write the sorted employees by name to another file, passing the location of the output file and list of sorted employee objects

    print("Employee data sorted by hourly salaries and written to file....")
    print("Employee data sorted by names and written to file....\n")
    
    #-----------------
    #binary search
    #-----------------
    employee_search = input("Enter the name of the employee to search - ") #prompt user for name of employee to search

    #call the binary search function passing it the name_list of employee objects(sorted by name), the seached employee, and the first index(low) and last index(high) of the list
    index = binary_search_by_name(name_list, employee_search, 0, len(name_list) - 1)

    if index != -1: #iif the function returns a valid index
        print(f"Employee found at index - {index}") #print the index where the employee was found
    else:
        print("Employee not found") #or esle print they werent found

#start the program
if __name__ == "__main__":
    main()
