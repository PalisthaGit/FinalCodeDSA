def linear_search(array, key):
    """
    Perform linear search to find the index of a key in the given array.
    If key is found, it is swapped with the first element of the array.

    Parameters:
        array (list): The list of integers to search.
        key (int): The key to search for.

    Returns:
        int: Index of the key if found, -1 otherwise.
    """
    # go through the array sequentially
    for i in range(len(array)):
        # check if the element is the key
        if array[i] == key:
            # swap the key element with the first element of the array
            array[0], array[i] = array[i], array[0]
            # return the original index of the key
            return i
    # return -1 if the key is not found
    return -1

array = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]
key = 4
result = linear_search(array, key)

if result == -1:
    print("Key not found")
else:
    print("Key found at index: ", result)

# print the updated array
print("Updated array: ", array)

# Output
# Key found at index:  5
# Updated array:  [4, 10, 5, 8, 7, 9, 11, 6, 15, 3]