# Queue coding problems
# Problem 1   -- Implement a Queue using Two Stacks

# Task: Design a Queue using two Stacks (push(x), pop(0), peek(), is_empty())

class QueueUsingStacks:
    def __init__ (self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        while self.stack1:    # if self.stack1 is not empty
            self.stack2.append(self.stack1.pop()) # keep removing elements one by one using .pop(), transferring them to self.stack2

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def pop(self):  # remove and return the front element of the queue
        if self.stack1:
            return self.stack1.pop()
        return None


    def peek(self):   
        if self.stack1:
            return self.stack1[-1]
        return None


    def is_empty(self):
        return len(self.stack1) == 0




""" Testing the Queue """
q = QueueUsingStacks()
q.push(1)
q.push(2)
q.push(3)
print(q.pop()) 
print(q.peek())
print(q.is_empty())
print(q.pop())
print(q.pop())
print(q.is_empty())