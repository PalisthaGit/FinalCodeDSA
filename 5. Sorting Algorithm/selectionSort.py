def selection_sort(array):
    
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]

data = [-2, 45, 0, 11, -9]
selection_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
