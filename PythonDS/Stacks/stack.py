class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    #O(1) - constant time
    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '. join(items)

        #0(1) contant time
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size+=1

    #0(1) constant time complexity 
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        pop_value = self.top.value
        self.top = self.top.next
        self.size-=1

        return pop_value
    
    #0(1) constant time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

if __name__ == '__main__' :
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(12)

    print(stack)

    stack.pop()

    stack.push(67)

    print(stack.peek())

    print(stack)