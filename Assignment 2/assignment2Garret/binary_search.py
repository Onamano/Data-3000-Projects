#binary_search.py

#defining the binary_search_by_name function, passing a list(name_list) of employee objects which is the 
#array of employees sorted by name using quicksort. It also gets passed the employee search target entered in by the user
#as well as the start point and end point of the array (low, high (current bounds of the search)), all of which are passed in from main.py when the function is called
def binary_search_by_name(employees, search_target, low, high):
    if low > high: #as the search range narrows, starting (low) and ending (high) point in the list get adjusted and if low is greater than high, that means the person being searched for is not in the list.
        return -1  #if there is nothing left to check, then return -1
    mid = low + (high - low) // 2 #calculating the middle index of thhe current search range
    mid_name = employees[mid].name.lower() #gets the employees name at the middle index and converts to lowercase
    search_target = search_target.lower() #converts the search target to lowercase

    if mid_name == search_target: #checks if the employee name located at the middle index is what the user has searched for
        #if it is that means we have found a match at the midpoint, 
        #but because there could be a duplicate earlier in the list, we search the left half to find the first occurance of the name
        left = binary_search_by_name(employees, search_target, low, mid - 1)
        return left if left != -1 else mid #if an earlier occurance is found return its index, left will be -1 if there is no earlier occuranc so return mid(the current index of the first occurance found)

    elif mid_name > search_target: #name of the person at the middle index is alphabetically after the search target, so we search the left half, setting the high point to the middle index -1
        return binary_search_by_name(employees, search_target, low, mid - 1)
    else: #if the name of the employee at the middle index is alphabetically before the search target, we search the right half, setting the low point to the middle index + 1 as we dont need to check that middle index again
        return binary_search_by_name(employees, search_target, mid + 1, high)  