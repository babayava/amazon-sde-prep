class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):  # push x to the back of THE QUEUE
        self.s1.append(x)

    
    def dequeue(self):                    # remove and return the element from the front of THE QUEUE
        if not self.s2:           # if self.s2 is empty 
            while self.s1:        # while self.s1 is not empty
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

    
    def peek(self):                            # return front element wo removing it
        if not self.s2:                  # if s2 is empty
             while self.s1:              # while s1 is not empty
                self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else None


    def empty(self):                # this method efficiently checks if the queue is empty in O(1) time.
        return not self.s1 and not self.s2



""" Testing the Queue """

q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.peek())
print(q.empty())