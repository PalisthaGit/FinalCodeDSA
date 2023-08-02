class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Adding data at the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Adding data at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    # Adding data after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    # Deleting a node
    def delete(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node == self.head:
                    self.head = cur_node.next
                cur_node = None
                return
            cur_node = cur_node.next

    # Printing the Doubly Linked List
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()


dllist = DoublyLinkedList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.append(45)
dllist.insert_after(dllist.head.next, 30)
dllist.print_list()  # Outputs: 62 8 30 12 45
dllist.delete(30)
dllist.print_list()  # Outputs: 62 8 12 45
