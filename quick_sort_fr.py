import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


def quick_sort(arr, low, high):
    if high > low:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def sort(arr):
    quick_sort(arr, 0, len(arr)-1)
