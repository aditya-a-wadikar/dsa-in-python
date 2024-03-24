def quickSort(arr):
    print(arr)

    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        greater = []
        lower = []

        for item in arr:
            if item > pivot:
                greater.append(item)
            else:
                lower.append(item)
            
    return quickSort(lower) + [pivot] + quickSort(greater)

        

array = [8, 2, 4, 7, 1, 3, 9, 6, 5]

arr = quickSort(array)
print(arr)