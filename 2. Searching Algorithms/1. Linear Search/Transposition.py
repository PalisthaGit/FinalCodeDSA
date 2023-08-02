# linear search in python
def linearSearch(array, key):
    
    # go through array sequentially
    for i in range(0, len(array)):
        
        # check if element is key
        if array[i] == key:
            
            # swap the element with its precedding element
            array[i], array[i - 1] = array[i - 1], array[i]

            # return index of key 
            return i
            
    return - 1
    
array = [9, 10 , 5, 8, 7, 4, 11, 6, 15, 3]
key = 4
n = len(array)
result = linearSearch(array, key)

if result == -1:
    print("Key not found")

else:
    print("Key found at index: ", result)

print("Updated array" , array)
