#quick_sort.py

# Function for sorting the list in the file using the quick sort method
def quick_sort_by_name(employees, low, high):
    if low < high:
        pivot_index = partition(employees, low, high)
        quick_sort_by_name(employees, low, pivot_index - 1)
        quick_sort_by_name(employees, pivot_index + 1, high)


def partition(employees, low, high):
    pivot = employees[high].name.lower()
    i = low - 1

    for j in range(low, high):
        if employees[j].name.lower() <= pivot:
            i += 1
            employees[i], employees[j] = employees[j], employees[i]

    employees[i + 1], employees[high] = employees[high], employees[i + 1]
    return i + 1