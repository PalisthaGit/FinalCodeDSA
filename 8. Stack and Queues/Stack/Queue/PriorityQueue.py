class PriorityQueue:
    def __init__(self):
        self.queue = []

    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        size = len(self.queue)

        if left < size and self.queue[left] > self.queue[largest]:
            largest = left

        if right < size and self.queue[right] > self.queue[largest]:
            largest = right

        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.heapify(largest)

    def insert(self, num):
        self.queue.append(num)
        size = len(self.queue)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(i)

    def delete(self, num):
        size = len(self.queue)
        for i in range(size):
            if num == self.queue[i]:
                self.queue[i], self.queue[size - 1] = self.queue[size - 1], self.queue[i]
                self.queue.pop()
                for i in range((size // 2) - 1, -1, -1):
                    self.heapify(i)
                return

        raise ValueError(f'{num} not found in queue')

    def print_queue(self):
        print("Max-Heap array: " + str(self.queue))


# Usage:
pq = PriorityQueue()
pq.insert(3)
pq.insert(4)
pq.insert(9)
pq.insert(5)
pq.insert(2)

pq.print_queue()

pq.delete(4)
print("After deleting an element: ")
pq.print_queue()
