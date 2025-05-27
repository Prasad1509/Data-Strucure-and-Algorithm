def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

arr = [5, 1, 4, 2, 8]

print(linear_search(arr, 5))  # Best case: found at index 0
print(linear_search(arr, 10)) # Worst case: not found, returns -1
