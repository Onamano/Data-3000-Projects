#selection_sort.py
#repeatedly finds smallest element from the unsorted portion and places it in its correct position

#defining the selection_sort_by_salary function that gets passed a list of employee objects to sort
#list is modified directly, no return needed
def selection_sort_by_salary(employees):
    number_of_employees = len(employees) #check how many employee objects are inside the list and store that value here

    #loop to move through each position in the list
    #current_index represents the position where the next smallest salary will be placed
    #everything before current_index is already sorted, and everything after is unsorted
    for current_index in range(number_of_employees):
        #at the start of each pass, we assume the employee at the current index has the smallest salary
        min_index = current_index

        #compare the assumed minimum with every other employee in the unsorted portion of the list
        #search_index goes over remaining unsorted elements after current_index
        for search_index in range(current_index + 1, number_of_employees):
            #compare salary of employee object at search_index with the employee at the min_index
            #calc_hourly_salary() calculates total salary for comparison
            if employees[search_index].calc_hourly_salary() < employees[min_index].calc_hourly_salary():
                #if we find an employee with a smaller salary than our surrent minimum, update min_index
                min_index = search_index
        #after checking all remaining unsorted objects min_index now holds the index of the employee with the smallest salary
        #swap the employee object at current_index with employee object at min_index
        #this places the smallst salary in the correct position in the sorted portion of the list
        employees[current_index], employees[min_index] = employees[min_index], employees[current_index]
    #after this swap, everything from index 0 to current_index is sorted and contains the smallest salaries in order