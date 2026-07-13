class Node :
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node with the given value to the end of the linked list
    # Time complexity is O(n) because we may need to traverse the entire list linearly to find the last node.
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
    