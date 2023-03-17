def selection_sort(array):
    index = 0
    for i in range(0, len(array) - 1):
        min = array[i]
        for j in range(i + 1, len(array) - 1):
            if array[j] < min:
                min = array[j]
                index = j
        temp = array[i]
        array[i] = min
        array[index] = temp


def sort(arr):
    selection_sort(arr)