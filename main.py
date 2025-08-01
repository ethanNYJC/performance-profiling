import timeit
import random

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

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start  # Index to insert

def insertionsort_binary(arr):
    n = len(arr)
    for i in range(1, n):
        target = arr[i]
        # 🔍 Find index where target should go
        pos = binary_search(arr, target, 0, i - 1)

        if arr[j] <= target:
            continue

        # ➡️ Shift elements to the right
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]

        arr[pos] = target

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


n = 100
arr = list(range(100))[1:]
random.shuffle(arr)

def test() -> int:
    """Test the performance of different sort algorithims on 1000 elements"""
    insertionsort_binary(arr.copy())

# Note that the function should be passed to `timeit.timeit` without '()'
# We don't want to call the function, instead we pass it to timeit.
# timeit will call the function (without arguments) and measure the time taken.
time = timeit.timeit(test, number=n)
print(f'Total time taken for {n} runs: {time}')
print("Average time taken (s):", time / n)
