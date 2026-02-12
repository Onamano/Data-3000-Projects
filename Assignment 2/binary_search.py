# binary_search.py

def binary_search_by_name(employees, target, low, high):
    """
    Recursive binary search on a list of employees sorted by name.
    """
    # Basic validation
    if not employees or target is None:
        return -1

    # Normalize target once
    target = target.strip().lower()
    if target == "":
        return -1

    # Base case: search space exhausted
    if low > high:
        return -1

    mid = (low + high) // 2

    # Ensure employee has a valid name
    try:
        mid_name = employees[mid].name.strip().lower()
    except (AttributeError, IndexError):
        return -1

    # If match found
    if mid_name == target:
        # Keep searching left
        left_index = binary_search_by_name(employees, target, low, mid - 1)
        return left_index if left_index != -1 else mid

    # If mid name is alphabetically greater go left
    elif mid_name > target:
        return binary_search_by_name(employees, target, low, mid - 1)

    # Otherwise go right
    else:
        return binary_search_by_name(employees, target, mid + 1, high)
