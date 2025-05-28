def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:]if x<pivot]
    right=[x for x in arr[1:]if x>=pivot]
    return quickSort(left)+[pivot]+quickSort(right)
arr=list(map(int,input("Enter The Numbers:").split()))
arr=quickSort(arr)
print("Sorted List:",arr)