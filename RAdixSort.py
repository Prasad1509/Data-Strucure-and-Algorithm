def counting_sort_place(arr, place):
    n = len(arr)
    count = [0] * 10
    output = [0] * n

    for num in arr:
        index = (num // place) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // place) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

arr = list(map(int, input("Enter numbers: ").split()))
max_num = max(arr)
place = 1

while max_num // place > 0:
    counting_sort_place(arr, place)
    place *= 10

print("Sorted list:", arr)
