import random
import time

import Insertion_Sort
import Merge_Sort
import heap_sort
import hybird_merge_selection
import quick_sort_fr
import selection_sort

array10m = range(10_000_000)

array1k = random.sample(array10m, 1_000)
array25k = random.sample(array10m, 25_000)
array50k = random.sample(array10m, 50_000)
array100k = random.sample(array10m, 100_000)
array250k = random.sample(array10m, 250_000)
array500k = random.sample(array10m, 500_000)
array1m = random.sample(array10m, 1_000_000)

arrays = [
    array1k,
    array25k,
    array50k,
    array100k,
    array250k,
    array500k,
    array1m,
]

m = 1_000_000
for i in range(len(arrays)):
    print("Array " + str(i + 1))


    array = arrays[i].copy()
    start_time = time.time()
    quick_sort_fr.sort(array)
    end_time = time.time()
    print("Quick Sort: " + str((end_time - start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    heap_sort.heap_sort(array)
    end_time = time.time()
    print("Heap Sort: " + str((end_time - start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    Insertion_Sort.InsertionSort(array)
    end_time = time.time()
    print("Insertion Sort: " + str((end_time-start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    Merge_Sort.mergesort(array,0,len(array)-1)
    end_time = time.time()
    print("merge sort: " + str((end_time-start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    selection_sort.selection_sort(array)
    end_time = time.time()
    print("selection Sort: " + str((end_time - start_time) * m) + "µs")

    array = arrays[i].copy()
    start_time = time.time()
    hybird_merge_selection.hybird_merge_selection(array,0,6,len(array)-1)
    end_time = time.time()
    print("Hybird merge: " + str((end_time - start_time) * m) + "µs")

    print()
