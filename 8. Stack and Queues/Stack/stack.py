class Stack:
    def __init__(self):
        self.stack = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Push an item to the stack
    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + str(item))

    # Pop an item from the stack
    def pop(self):
        if self.is_empty():
            return "stack is empty"

        return self.stack.pop()

    # Display the stack
    def display(self):
        return self.stack


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("popped item: " + str(stack.pop()))
print("stack after popping an element: " + str(stack.display()))
