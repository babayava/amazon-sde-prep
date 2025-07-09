# Implementing a Stack using a Python List //StackPythonList//

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())