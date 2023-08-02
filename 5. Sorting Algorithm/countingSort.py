def counting_sort(array):
    size = len(array)
    output = [0] * size

    # Find the maximum element to know the count array size
    max_val = max(array)

    # Initialize count array
    count = [0] * (max_val + 1)

    # Store the count of each elements in count array
    for i in range(size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)
