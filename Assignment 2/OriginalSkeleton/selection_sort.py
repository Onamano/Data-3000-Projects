#selection_sort.py

def selection_sort_by_salary(employees):
    n = len(employees)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if employees[j].calc_hourly_salary() < employees[min_index].calc_hourly_salary():
                min_index = j

        employees[i], employees[min_index] = employees[min_index], employees[i]
