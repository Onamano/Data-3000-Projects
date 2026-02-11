#binary_search.py

def binary_search_by_name(employees, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    mid_name = employees[mid].name.lower()
    target = target.lower()

    if mid_name == target:
        #keep searching left to find first occurrence
        left = binary_search_by_name(employees, target, low, mid - 1)
        return left if left != -1 else mid

    elif mid_name > target:
        return binary_search_by_name(employees, target, low, mid - 1)
    else:
        return binary_search_by_name(employees, target, mid + 1, high)