def merge(left, right):
    merged_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i+=1
        else:
            merged_array.append(right[j])
            j+=1
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        merged_array = merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
        return merged_array

arr = [2, 8, 5, 3, 9, 4, 1]
merged_array = mergeSort(arr)
print(merged_array)
