import timeit
import random
import math

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            return arr

    return arr

def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        target = arr[i]
        j = i-1

        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = target

    return arr

def merge(left, right):
    sorted_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))

    return sorted_arr + left + right


def mergesort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    
    # split the array into left and right subarrays
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort each subarray
    left_arr = mergesort(left)
    right_arr = mergesort(right)

    # merge the subarrays into a sorted array
    return merge(left_arr, right_arr)
    
def quicksort(arr: list):
    # handle base case
    if len(arr) <= 1:
        return arr
    
    # select pivot
    pivot = arr.pop()

    # split remaining elements into less-than and greater-than subarrays by comparing with pivot
    lt_arr = []
    mt_arr = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            lt_arr.append(arr[i])
        else:
            mt_arr.append(arr[i])


    # recursively sort subarrays
    # concatenate less-than subarray, pivot, more-than array
    return quicksort(lt_arr) + [pivot] + quicksort(mt_arr)

def round_sig_figs(num, sig_figs):
    if num == 0:
        return 0
    return round(num, sig_figs - int(math.floor(math.log10(abs(num)))) - 1)


def test(size) -> int:
    arr = list(range(size))
    random.shuffle(arr)
    mergesort(arr)

n = 20
timedict = {}
for size in [10, 100, 1000, 10000]:
    time = timeit.timeit(lambda: test(size), number=n)
    timedict[f'{size} runs'] = round_sig_figs(time, 3) / n

print(timedict)