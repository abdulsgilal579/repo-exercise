def find_smallest_int(arr):
    if not arr:
        return None
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest
smallest_int = find_smallest_int([34, 15, 88, 2])         
print(smallest_int)