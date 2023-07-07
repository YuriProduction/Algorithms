def binary_search(list_: list, item):
    law = 0
    high = len(list_) - 1
    while law <= high:
        mid = (law + high) // 2
        if list_[mid] == item:
            return mid
        elif list_[mid] > item:
            high = mid
        elif list_[mid] < item:
            law = mid
    return None


temp = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(temp, 11))
