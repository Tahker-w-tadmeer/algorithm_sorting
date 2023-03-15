def selection_sort(array):
    index = 0
    for i in range(0, len(array) - 1):
        min = array[i]
        for j in range(i + 1, len(array) - 1):
            if (array[j] < min):
                min = array[j]
                index = j
        temp = array[i]
        array[i] = min
        array[index] = temp


arrr = [2, 99, 635, -589, 6453, -545, 33, 9, 6, 8, 87, 10, 100, 150, 190, 1000, 9000]
selection_sort(arrr)
print(arrr)
