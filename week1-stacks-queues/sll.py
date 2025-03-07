#we can build a Stack using a LinkedList for better performance
#in large-scale applications. //StackLinkedList//

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #pointer to the next node

class Stack:
    def __init__(self):
        self.top = None # top of the stack

    def push(self, value): # push item to the top of the stack
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):  # remove and return the top item
        if self.is_empty():
            return "Stack is empty"
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self): # returns the top item
        if self.is_empty():
            return "Stack is empty"
        return self.top.value
    
    def is_empty(self):  # Check if the stack is empty
        return self.top is None

""" Testing the Stack"""
stack = Stack()
stack.push(5)
stack.push(15)
stack.push(25)

print(stack.pop())
print(stack.peek())
print(stack.is_empty())
