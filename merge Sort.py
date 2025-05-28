def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i < len(left) and j<len(right):
            arr[k]=left[i] if left[i]<right[j] else right[j]
            if left[i]<right[j]:
                i+=1
            else:
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

arr=list(map(int,input("Enter The Numbers:").split()))
mergeSort(arr)
print(arr)