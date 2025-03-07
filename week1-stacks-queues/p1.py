# Problem 1: Implement a Stack with a getMin() Method
# Task: Design a stack that supports push(x), pop(), peek(),
#       and getMin(), which returns the smallest element in constant time (O(1)).


class MinStack:
    def __init__ (self):
        self.stack = []     # main stack
        self.min_val = []   # stack to track min values

    def push(self, value):
        self.stack.append(value)
        if not self.min_val or value <=self.min_val[-1]: # if min stack is empty or new val is smaller, push it.
            self.min_val.append(value)

    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            if popped_value == self.min_val[-1]:
                self.min_val.pop()
            return popped_value
        return "Stack is empty"
             
    def peek(self): 
        if self.stack:
            return self.stack[-1]
        return "Stack is empty"

    def getMin(self): # returns minimum value in O(1)
        if self.min_val:
            return self.min_val[-1]
        return "Stack is empty"
        
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
print(stack.getMin())
stack.pop()
print(stack.getMin())
    