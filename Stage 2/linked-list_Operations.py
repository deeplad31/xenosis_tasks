class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        previous = None

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to be deleted
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key was not present in the linked list
        if not current:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
print("Traversal after insertion:")
ll.traverse()

ll.delete(2)
print("Traversal after deletion of 2:")
ll.traverse()

ll.delete(1)
print("Traversal after deletion of 1:")
ll.traverse()

ll.delete(3)
print("Traversal after deletion of 3:")
ll.traverse()

ll.delete(4)
print("Traversal after deletion of 4:")
ll.traverse()