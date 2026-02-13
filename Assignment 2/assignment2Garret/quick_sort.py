#quick_sort.py

#function to perform quick sort on list of employee objects based on their name attribute
#expects list of employee objects, starting index and ending index of list to sort
def quick_sort_by_name(employees, low, high):
    #if low >= high, the sub-array has 0 or one element and doesnt need to be sorted
    if low < high:
        #call partition function passing employee list and start and end index
        pivot_index = partition(employees, low, high)
        quick_sort_by_name(employees, low, pivot_index - 1) #apply quicksort to the left sub-array(before pivot)
        quick_sort_by_name(employees, pivot_index + 1, high) #apply quicksort to the right sub-array(after pivot)

#partition function rearanges elements <= pivot are on the left and elements > pivot are on the right
#returns index where the pivot element ends up
def partition(employees, low, high):
    pivot = employees[high].name.lower() #choose last element in sub-array as the pivot, converting name to lowercase
    last_smaller_index = low - 1 #initialize boundary index for elements smaller than or equal to the pivot, starts at low -1 because no elements have been checked yet

    #loops through all elements in sub-array except the pivot itself
    for current_index in range(low, high): 
        if employees[current_index].name.lower() <= pivot: #if current employees name is alphabetically <= pivot
            last_smaller_index += 1 #move the boundary forward to include this smaller/equal emelemt 

            #swap current element with element at boundary index
            #ensures all elements <= pivot are on left
            employees[last_smaller_index], employees[current_index] = employees[current_index], employees[last_smaller_index]

    #after loop, place pivot in correct sorted position 
    #swap the element after the last smaller element with the pivot 
    employees[last_smaller_index + 1], employees[high] = employees[high], employees[last_smaller_index + 1]
    #return final index of the pivot element
    return last_smaller_index + 1 