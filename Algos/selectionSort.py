def selectionSort(arr):
    length = len(arr)
    if length <= 0:
        return arr
    else:
        for i in range(length):
            tmin = i
            for j in range(i, length):
                if arr[j] < arr[tmin]:
                    tmin = j
            if tmin != i:
                arr[tmin], arr[i] = arr[i], arr[tmin]
        return arr

case1 = []
case2 = [1]
case3 = [2, 1]
case4 = [6, 5, 3, 1, 8, 7, 2, 4]
case5 = [1, 2, 3, 4, 5, 6, 7, 8]

# add testcases from here

cases = [case1, case2, case3, case4, case5]

for case in cases:
    try:
        tested_case = selectionSort(case)
        print(tested_case)
    except Exception as e:
        print(e)
