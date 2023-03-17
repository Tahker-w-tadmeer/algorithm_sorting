def selection_sort(array, start, end):
    index = start
    for i in range(start, end + 1):
        min = array[i]
        for j in range(i, end + 1):
            if array[j] < min:
                min = array[j]
                index = j
        if array[i] > min:
            temp = array[i]
            array[i] = min
            array[index] = temp


def hybird_merge_selection(array, start, thershold, end):
    size = end - start
    if size > thershold > 0:
        mid = (start + end) // 2
        hybird_merge_selection(array, start, thershold, mid)
        hybird_merge_selection(array, mid + 1, thershold, end)

    selection_sort(array, start, end)


def sort(arr):
    hybird_merge_selection(arr, 0, 10, len(arr) - 1)
