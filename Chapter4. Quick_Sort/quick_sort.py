def quick_sort(arr: list):
    """O(n*log(n))"""
    if len(arr) < 2:
        return arr
    oporniy = arr[0]
    less_oporniy = [i for i in arr[1:] if i <= oporniy]
    bigger_oporniy = [i for i in arr[1:] if i > oporniy]
    return quick_sort(less_oporniy) + [oporniy] + quick_sort(bigger_oporniy)


arr_to_test = [5, 1, 2, 16, 13, 12, 19, 20, 1, 4, 7, 8, 9, 3, 39]
print(quick_sort(arr_to_test))