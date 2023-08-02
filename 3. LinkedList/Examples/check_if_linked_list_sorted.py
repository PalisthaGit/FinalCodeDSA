def isSorted(self):

    # set current node to head node
    current = self.head
    # set a minimum value for the previous node
    prev_node = -234324

    # continue till end of linked list
    while current != None:
        # stop the loop if current is greater than prev_node
        if (current.data < prev_node):
            # return False if the list is not sorted in ascending order
            return False

        # assign the data of current node to prev_node
        prev_node = current.data

        # move current to succedding node
        current = current.next

    # return true if we reach end of the linked list, meaning the list is sorted
    return True
