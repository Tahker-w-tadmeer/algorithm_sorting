def merge(array, left, mid, right):
    nleft = mid - left + 1
    nright = right - mid

    al = array[left:mid + 1]
    ar = array[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < nleft and j < nright:
        if al[i] <= ar[j]:
            array[k] = al[i]
            i = i + 1
            k = k + 1

        else:
            array[k] = ar[j]
            j = j + 1
            k = k + 1

    while i < nleft:
        array[k] = al[i]
        i = i + 1
        k = k + 1

    while j < nright:
        array[k] = ar[j]
        j = j + 1
        k = k + 1


def mergesort(temp, first, last):
    if first < last:
        mid = (first + last) // 2
        mergesort(temp, first, mid)
        mergesort(temp, mid + 1, last)
        merge(temp, first, mid, last)


def sort(arr):
    mergesort(arr, 0, len(arr) - 1)
