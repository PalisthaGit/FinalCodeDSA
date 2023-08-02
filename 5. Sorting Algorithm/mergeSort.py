def merge_sort(input_list):
    if len(input_list) > 1:

        # Find the middle point of the list
        middle = len(input_list) // 2
        left_half = input_list[:middle]
        right_half = input_list[middle:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1

        # If there are remaining elements, add them to the list
        while i < len(left_half):
            input_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_list[k] = right_half[j]
            j += 1
            k += 1


def print_list(input_list):
    for i in range(len(input_list)):
        print(input_list[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    input_list = [6, 5, 12, 10, 9, 1]

    merge_sort(input_list)

    print("Sorted list is: ")
    print_list(input_list)
