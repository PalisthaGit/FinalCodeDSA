class CircularQueue:
    def __init__(self, k):
        """Initialize a new circular queue with capacity k."""
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def push(self, data):
        """Insert an element into the circular queue."""
        if ((self.tail + 1) % self.k == self.head):
            raise Exception("The circular queue is full")
        elif (self.head == -1):
            self.head = self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def pop(self):
        """Remove an element from the circular queue."""
        if (self.head == -1):
            raise Exception("The circular queue is empty")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def print_queue(self):
        """Print the elements in the circular queue."""
        if(self.head == -1):
            print("No element in the circular queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Example usage:
obj = CircularQueue(5)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("Initial queue")
obj.print_queue()

obj.pop()
print("After removing an element from the queue")
obj.print_queue()
