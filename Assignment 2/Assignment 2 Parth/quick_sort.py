# quick_sort.py

def quick_sort_by_name(employees, low, high):
    """
    Recursive Quick Sort on employees list, sorted by name (case-insensitive).
    """
    if not employees:
        return  # Nothing to sort

    if low < high:
        pivot_index = partition(employees, low, high)
        quick_sort_by_name(employees, low, pivot_index - 1)
        quick_sort_by_name(employees, pivot_index + 1, high)


def partition(employees, low, high):
    """
    Partitions the list around a pivot (last element).
    Elements <= pivot go left, others go right.
    """

    try:
        pivot = employees[high].name.strip().lower()
    except (AttributeError, IndexError):
        return low  # Fail safely if bad data

    i = low - 1

    for j in range(low, high):
        try:
            current_name = employees[j].name.strip().lower()
        except AttributeError:
            continue  # Skip invalid entries instead of crashing

        if current_name <= pivot:
            i += 1
            employees[i], employees[j] = employees[j], employees[i]

    # Place pivot in correct sorted position
    employees[i + 1], employees[high] = employees[high], employees[i + 1]

    return i + 1
