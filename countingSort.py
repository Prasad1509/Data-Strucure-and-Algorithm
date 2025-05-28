arr = list(map(int, input("Enter numbers: ").split()))

max_val = max(arr)
count = [0] * (max_val + 1)

for num in arr:
    count[num] += 1

sorted_arr = []
for i in range(len(count)):
    sorted_arr.extend([i] * count[i])

print("Sorted list:", sorted_arr)
