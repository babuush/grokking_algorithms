def binary_search(list_input, item):
    low = 0
    high = len(list_input) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_input[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 6, 7]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))