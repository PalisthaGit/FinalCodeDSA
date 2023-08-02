def linear_search(array, key):
    """
    Perform linear search to find the index of a key in the given array.

    Parameters:
        array (list): The list of integers to search.
        key (int): The key to search for.

    Returns:
        int: Index of the key if found, -1 otherwise.
    """
    # go through the array sequentially
    for i in range(len(array)):
        # check if element is the key
        if array[i] == key:
            # return the index of the key
            return i
    # return -1 if the key is not found
    return -1

# create an array with a list of integers
array = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]

# take user input for the key to search in the array
key = int(input("Enter the key to search for: "))

# call the linear_search function and store the result in the result variable
result = linear_search(array, key)

# check if the key was found or not and print the appropriate message
if result == -1:
    print("Key not found")
else:
    print("Index of the key:", result)
