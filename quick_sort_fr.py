import random


def partition(arr, low, high):
    pivot = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def random_partition(arr, low, high):
    random_pivot = random.randrange(low, high)
    arr[low], arr[random_pivot] = arr[random_pivot], arr[low]
    return partition(arr, low, high)


def quick_sort(arr, low, high):
    if high > low:
        pivot = random_partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


for z in range(10):
    x = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    quick_sort(x, 0, len(x) - 1)
    print(x)
