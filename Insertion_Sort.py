def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

a = [2,99,635,-589,6453,-545,33,9,6,8,87,10,100,150,190,1000,9000,0]
sorted_list = InsertionSort(a)
print(a)