# Stack 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Stack usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1

# Queue usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2