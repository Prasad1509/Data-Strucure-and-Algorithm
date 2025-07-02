list1 = sorted(list(map(int, input("Enter numbers: ").split())))
key = int(input("Enter number to search: "))

low, high = 0, len(list1) - 1

while low <= high:
    mid = (low + high) // 2
    if list1[mid] == key:
        print("Element found at index:", mid)
        break
    elif list1[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
