list1 = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter number to search: "))

for i in range(len(list1)):
    if list1[i] == key:
        print("Element found at index:", i)
        break
else:
    print("Element not found")
