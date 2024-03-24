def insertionSort(arr):
    length = len(arr)
    if length < 1:
        return arr
    else:
        for i in range(1, length):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
        return arr


# -------------
case1 = []
case2 = [1]
case3 = [2, 1]
case4 = [6, 5, 3, 1, 8, 7, 2, 4]
case5 = [1, 2, 3, 4, 5, 6, 7, 8]
# add testcases from here

cases = [case1, case2, case3, case4, case5]
# cases = [case4]

for case in cases:
    try:
        tested = insertionSort(case)
        print(tested)
        
    except Exception as e:
        print(e)
