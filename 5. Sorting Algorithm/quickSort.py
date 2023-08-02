# Function to find the partition position
def partition(input_list, low, high):

  # Choose the rightmost element as pivot
  pivot = input_list[high]

  # Pointer for greater element
  i = low - 1

  # Traverse through all elements, comparing each with the pivot
  for j in range(low, high):
    if input_list[j] <= pivot:
      # If an element smaller than the pivot is found, swap it with the 
      # "greater" element pointed to by 'i'
      i += 1
      # Swapping element at 'i' with element at 'j'
      (input_list[i], input_list[j]) = (input_list[j], input_list[i])

  # Swap the pivot element with the greater element specified by 'i'
  (input_list[i + 1], input_list[high]) = (input_list[high], input_list[i + 1])

  # Return the position where partition is done
  return i + 1

# Function to perform quicksort
def quick_sort(input_list, low, high):
  if low < high:

    # Find pivot element such that elements smaller than pivot are on the left
    # and elements greater than pivot are on the right
    pivot_index = partition(input_list, low, high)

    # Recursive call on the part of the array before pivot
    quick_sort(input_list, low, pivot_index - 1)

    # Recursive call on the part of the array after the pivot
    quick_sort(input_list, pivot_index + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array:")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
