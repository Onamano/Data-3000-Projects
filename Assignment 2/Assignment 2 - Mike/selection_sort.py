#selection_sort.py

def selection_sort_by_salary(employees):
    employeesSize = len(employees)

    # Iterates through the list and selects the smallest salary to sort into the smallest salary into an earlier position until the value is in the correct position, swapping each time as needed until the list is completely sorted by salary
    for i in range(employeesSize):
        min_index = i
        for j in range(i + 1, employeesSize):
            if employees[j].calc_hourly_salary() < employees[min_index].calc_hourly_salary():
                min_index = j

        # Resets the index to the smallest value each time a number is sorted
        employees[i], employees[min_index] = employees[min_index], employees[i]
