def binary_search(array, key):
    # set low to first element
    low = 0
    
    # set high to last element
    high = len(array) - 1
    
    # iterate until low is less than or equal to high
    while low <= high:
        mid = (low + high ) // 2
        
        if key == array[mid]:
            return mid
        
        elif key < array[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
    
    # if key is not found
    return -1

array = [4, 5, 6, 7, 8, 9, 10]
key = 5
result = binary_search(array, key)

if result == -1:
    print("Not found")
else:
    print("Element is present at index: ", result)

# Output
# Element is present at index:  1
