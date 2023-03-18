import quick_sort_fr
import random
import quick_sort_fr


def find_kth_element(arr, low, high, element):
    if high > low:
        pivot = quick_sort_fr.partition(arr, low, high)
    if pivot == element:
        return arr[pivot]
    if pivot < element:
        find_kth_element(arr, pivot - 1, high, element)
    if pivot > element:
        find_kth_element(arr, low, pivot - 1, element)
