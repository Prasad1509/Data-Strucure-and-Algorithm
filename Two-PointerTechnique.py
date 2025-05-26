# Q: How to check if a list has a pair that sums to a target using two pointers?
def has_pair_with_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair_with_sum([10, 5, 3, 7], 190))  
