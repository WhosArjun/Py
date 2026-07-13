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
    
    # Prepend a new node with the given value to the beginning of the linked list
    # Time complexity is O(1) because we are adding the new node at the beginning
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
    
    