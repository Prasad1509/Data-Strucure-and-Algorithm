def find_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

print(find_duplicates([1, 2, 3, 4, 2]))  
