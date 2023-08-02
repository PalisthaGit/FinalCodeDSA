# remove duplicate from the sorted linked list
def remove_duplicate(self):
    # set current node to the head
    current = self.head
    # set next_node to the node after current
    next_node = current.next

    # loop through the linked list
    while next_node != None:
        # if data of current node is not equal to data of next_node
        if current.data != next_node.data:
            # move current to the next node
            current = next_node
            # set next_node to the node after current
            next_node = next_node.next

        # if data of current node is equal to data of next_node
        else:
            # set next node of current node to the node after next_node
            current.next = next_node.next
            # delete next_node
            del next_node
            # set next_node to the node after current node
            next_node = current.next
