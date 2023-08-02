def find_max(self):
    # start at the head of the list
    current = self.head
    # initialize max_val to a small value
    max_val = -99999999
    # iterate through each node in the list
    while current:
        # if the current node's data is greater than max_val
        if current.data > max_val:
            # update max_val with the current node's data
            max_val = current.data
        # move to the next node
        current = current.next
    # return the maximum value
    return max_val