class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index

    def heapify_down(self, index):
        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)
            if self.has_right_child(index) and self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop(-1)  # Pop the last element and set it as root
        self.heapify_down(0)
        return root

# Example implementation
heap = MinHeap()
list1 = [15, 16, 25, 5, 12]
heap.heapify(list1)
print(heap)  # Output will be: [5, 12, 25, 16, 15]
