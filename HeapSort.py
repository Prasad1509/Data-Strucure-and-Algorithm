import heapq
arr=list(map(int,input("Enter The Numbers:").split()))
heapq.heapify(arr)
sortedArr=[heapq.heappop(arr) for _ in range(len(arr))]
print("Sorted list:",sortedArr)