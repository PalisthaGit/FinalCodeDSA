def binary_search(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        # Search the right half
        else:
            return binary_search(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search(array, x, 0, len(array)-1)

if result == -1:
    print("Not found")
else:
    print("Element is present at index " + str(result))  


# Output
# Element is present at index 1
