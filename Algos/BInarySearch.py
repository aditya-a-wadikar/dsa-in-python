arr = [1, 3, 5, 7, 9, 11, 13, 15]

def binarySearch(arr:list, find):
    left, right= 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == find:
            return mid
        elif find < arr[mid]:
            right = mid-1
        else:
            left = mid+1

# print(binarySearch(arr, 9))        



# find mininum in sorted rotated array
def findMin(arr):
    lo, hi = 0, len(arr)-1
    rotation = 0

    while lo<hi:
        mid = (lo + hi)//2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
        rotation +=1

    print(arr[lo], f'rotated {lo} times')


arr1= [11, 12, 15, 18, 2, 5, 6, 8]
arr2 = [3,4,5,1,2]
arr3 = [11,13,15,17]
arrs = [arr1, arr2, arr3]
for arr in arrs:
    findMin(arr)