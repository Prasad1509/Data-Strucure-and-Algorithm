def ternary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < mid1:
            high = mid1 - 1
        elif key > mid2:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1

arr = sorted(list(map(int, input("Enter sorted numbers: ").split())))
key = int(input("Enter number to search: "))

index = ternary_search(arr, key)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
