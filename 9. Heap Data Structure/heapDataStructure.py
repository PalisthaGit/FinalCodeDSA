class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        size = len(self.heap)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def insert(self, num):
        self.heap.append(num)
        size = len(self.heap)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(i)

    def delete(self, num):
        size = len(self.heap)
        for i in range(size):
            if num == self.heap[i]:
                self.heap[i], self.heap[size - 1] = self.heap[size - 1], self.heap[i]
                self.heap.pop()
                for i in range((size // 2) - 1, -1, -1):
                    self.heapify(i)
                return

        raise ValueError(f'{num} not found in heap')

    def print_heap(self):
        print("Max-Heap array: " + str(self.heap))


# Usage:
mh = MaxHeap()
mh.insert(3)
mh.insert(4)
mh.insert(9)
mh.insert(5)
mh.insert(2)

mh.print_heap()

mh.delete(4)
print("After deleting an element: ")
mh.print_heap()
