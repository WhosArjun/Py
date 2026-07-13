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
    

    # Insert a new node with the given value at the specified index in the linked list
    # Time complexity is O(n) because we may need to traverse the entire list linearly to find the node at the specified index.
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        else:
            if self.head is None:
                raise IndexError("Index out of bounds")
            else:
                last = self.head

                for i in range(index - 1):
                    if last.next is None:
                        raise IndexError("Index out of bounds")
                    last = last.next
                
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    # Remove the first occurrence of a node with the given value from the linked list
    # Time complexity is O(n) because we may need to traverse the entire list linearly to find the node with the specified value.
    def __contains__(self, value):
        last = self.head  #Last contains the heading element
        while last is not None: #While the current element is not None(null)
            if last.value == value: #If the current value is equal to the value parameter
                return True #Return true
            last = last.next #Update the increment of the element in the linkedlist
        return False #Return false if the element isnt contained in the linked list
    
    #Return the length of the linked list
    # Time complexity is O(n) because we need to traverse the entire list linearly to count the number of nodes.
    def len(self):
        i = 0  #Increment variable
        last = self.head #Initialize last to the head of the linked list
        while last is not None: #While the current element is not None(null)
            i+=1 #Increment the counter
            last = last.next #Increment the current value to the next not-None value
        return i #Return the increment length
    
    # Remove the first occurrence of a node with the given value from the linked list
    # Time complexity is O(n) because we may need to traverse the entire list linearly to find the node with the specified value.
    def delete(self, value):
        last = self.head #Initialize last to the head of the linked list
        while last is not None: #While the current element is not None(null)
            if last.value == value: #If the current value is equal to the value parameter
                self.head = last.next #Update the head of the linked list to the next value
            else:  
                while last.next: #While the next value is not None(null)
                    if last.next.value == value: #If the next value is equal to the value parameter
                        last.next = last.next.next  #Update the next value to the next value of the next value
