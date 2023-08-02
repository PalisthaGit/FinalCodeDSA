def reverselinkedlist(self):
    # Create an empty list to store the values of the linked list
    values = []
    # Traverse the linked list and store each node's data in the list
    current = self.head
    while current:
        values.append(current.data)
        current = current.next
    # Traverse the linked list again and replace each node's data with the values from the reversed list
    current = self.head
    i = len(values) - 1
    while current:
        current.data = values[i]
        current = current.next
        i -= 1
