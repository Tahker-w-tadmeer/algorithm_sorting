def max_heapify(arr, N, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < N and arr[left] > arr[largest]:
        largest = left
    if right < N and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)


def heapify(arr):
    leaf = (len(arr) // 2) - 1

    for i in range(leaf, -1, -1):
        max_heapify(arr, len(arr), i)


def heap_sort(arr):
    heapify(arr)
    N = len(arr)
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


arr = [1, 10, 20, 400, 2]
heap_sort(arr)
# arr.reverse()
print(arr)
