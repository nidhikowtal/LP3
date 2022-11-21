# Python implementation QuickSort using
# Hoare's partition Scheme.

import random

'''
The function which implements randomised
QuickSort, using Haore's partition scheme.
arr :- array to be sorted.
low :- starting index of the array.
high :- ending index of the array.
'''

def quicksort(arr, low, high):
    if(low < high):
        pivotindex = partitionrand(arr,low, high)
        
        quicksort(arr , low , pivotindex)
        quicksort(arr, pivotindex + 1, high)

'''
This function generates random pivot,
swaps the first element with the pivot
and calls the partition f
unction.
'''

def partitionrand(arr , low, high):
    randpivot = random.randrange(low, high)
    
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition(arr, low, high)

'''
This function takes the first element
as pivot, places the pivot element at
the correct position in the sorted array.
All the elements are re-arranged according
to the pivot, the elements smaller than
the pivot is places on the left and
the elements greater than the pivot is
placed to the right of pivot.
'''
def partition(arr,low,high):
    pivot = low # pivot
    i = low - 1
    j = high + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]
        
array = [10, 7, 8, 9, 1, 5]
quicksort(array, 0, len(array) - 1)
print(array)
