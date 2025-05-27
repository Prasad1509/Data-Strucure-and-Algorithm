def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

arr = [3, 5, 2, 9, 4]
print(linear_search(arr, 9)) 
