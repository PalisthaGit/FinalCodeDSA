class Deque:
    def __init__(self):
        """Initialize a new deque."""
        self.items = []

    def is_empty(self):
        """Check if the deque is empty."""
        return not bool(self.items)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque."""
        if not self.is_empty():
            return self.items.pop(0)
        raise Exception("Deque is empty")

    def remove_rear(self):
        """Remove an item from the rear of the deque."""
        if not self.is_empty():
            return self.items.pop()
        raise Exception("Deque is empty")

    def size(self):
        """Return the number of items in the deque."""
        return len(self.items)


# Example usage:
d = Deque()
print(d.is_empty())
d.add_rear(8)
d.add_rear(5)
d.add_front(7)
d.add_front(10)
print(d.size())
print(d.is_empty())
d.add_rear(11)
print(d.remove_rear())
print(d.remove_front())
d.add_front(55)
d.add_rear(45)
print(d.items)
