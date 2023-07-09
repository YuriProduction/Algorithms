def find_smallest(arr: list):
    """Complexity: O(n)"""
    smallest_el = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr) - 1):
        if arr[i] < smallest_el:
            smallest_el = arr[i]
            smallest_ind = i
    return smallest_ind


def sort_by_choice(arr: list):
    """Complexity: O(n^2)"""
    new_arr = []
    for i in range(len(arr) - 1):  # n раз по массиву
        smallest_ind = find_smallest(arr)  # n раз находим наименьший
        new_arr.append(arr.pop(smallest_ind))  # pop работает за O(n)
    return new_arr


arr = [7, 5, 9, 2, 3, 1, 11, 17]
print(sort_by_choice(arr))
