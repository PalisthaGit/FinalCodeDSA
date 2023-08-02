# create Node for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def count_elements(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_node(self, index, x):
        if index < 1 or index > self.count_elements():
            return
        new_node = Node(x)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(0, index-2):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_node(self, index):
        prev_node = None
        if index < 1 or index > self.count_elements():
            return -1
        if index == 1:
            prev_node = self.head
            self.head = self.head.next
            del prev_node
        else:
            current = self.head
            for i in range(index - 1):
                prev_node = current
                current = current.next
            prev_node.next = current.next
            del current

# create an instance of LinkedList
linked_list = LinkedList()
linked_list.create_linked_list()
linked_list.append(18)
linked_list.insert_node(3, 11)
linked_list.delete_node(1)
linked_list.traverse_list()

# Output
# 9
# 11
# 14
# 18