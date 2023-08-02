class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def display(self):
        return self.queue

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Queue: ", q.display())

q.dequeue()

print("After dequeuing, Queue: ", q.display())
