# bubble sort algo
def bubbleSort(arr):
    if len(arr) <= 1:
        return arr

    else:  
        did_swap = False
        length = len(arr)
        for i in range(length-1):
            for j in range(length-i-1):
                if arr[j] > arr[j+1]:
                    did_swap = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            if not did_swap:
                print('array is already sorted')
                break
        return arr

                    
        
# ----------------------------------------------------

case1 = []
case2 = [1]
case3 = [2, 1]
case4 = [6, 5, 3, 1, 8, 7, 2, 4]
case5 = [1, 2, 3, 4, 5, 6, 7, 8]
# add testcases from here

cases = [case1, case2, case3, case4, case5]

for case in cases:
    try:
        tested = bubbleSort(case)
        print(tested)
        
    except Exception as e:
        print(e)

        
