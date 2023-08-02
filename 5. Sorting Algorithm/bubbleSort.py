def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j] 
                swapped = True
        if not swapped:
            break  # Stop iteration if the array is sorted.

data = [-2, 45, 0, 11, -9]
bubble_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
